"""
Few words from author about mixedCase methods and functions naming:

I'm sorry about my mixedCase methods and functions naming,
i know PEP8 and that function names should be lowercase, with words separated by underscores.
But mixedCase is used at my recent projects as prevailing style (e.g. like in threading.py),
so I decided to use the same familiar for me naming as I used before.
"""
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from math import sqrt
from pprint import pformat
from copy import deepcopy
from itertools import chain, izip, product


class CommonEqualityMixin(object):
    """ May not be used in my implementation, if __hash__ will be overrided to use set below. """
    def __eq__(self, other):
        return (isinstance(other, self.__class__)
            and self.x == other.x and self.y == other.y)

    def __ne__(self, other):
        return not self.__eq__(other)


class PostalCode(CommonEqualityMixin):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

    def __str__(self):
        return "<PostalCode name: {name} x: {x} y: {y}>".format(**self.__dict__)

    __repr__ = __str__

    def __hash__(self):
        """ Override the default hash behavior (that returns the id or the object) to use set below. """
        return hash((self.x, self.y))


class PostalCodesContainer(object):
    def __init__(self, allCodes, maxNodeSize):
        self.allCodes = allCodes
        self.maxNodeSize = maxNodeSize
        self._validateCodesLen()
        self._validateMaxSize()

    def _validateCodesLen(self):
        if len(self.allCodes) <= 1:
            raise ValueError("Please insert more postal codes")

    def _validateMaxSize(self):
        for point in self.allCodes:
            if not AABBHelper.containsPoint(self.maxNodeSize, point.x, point.y):
                raise RuntimeError("Invalid point position: {} maxNodeSize: {}".format(point, self.maxNodeSize))


class AABBHelper(object):
    @staticmethod
    def containsPoint(size, x, y):
        x0, y0, x1, y1 = size
        if x0 <= x <= x1 and y0 <= y <= y1:
            return True
        return False

    @staticmethod
    def quadDivide(size):
        x0, y0, x1, y1 = size
        h = (x1 - x0) / 2.0
        return [
            (x0, y0, x0 + h, y0 + h),
            (x0, y0 + h, x0 + h, y1),
            (x0 + h, y0 + h, x1, y1),
            (x0 + h, y0, x1, y0 + h)
        ]

    @staticmethod
    def getIntersection(nodeOne, nodeTwo):
        x0, y0, x1, y1 = nodeOne.size
        x2, y2, x3, y3 = nodeTwo.size
        points = (x0, y0), (x1, y1), (x2, y2), (x3, y3)
        A, B, A1, B1 = points
        sorted_x = sorted([c[0] for c in points])
        sorted_y = sorted([c[1] for c in points])
        if (abs(B[0] - A[0]) + abs(B1[0] - A1[0]) >= abs(sorted_x[3] - sorted_x[0])) and \
                (abs(B[1] - A[1]) + abs(B1[1] - A1[1]) >= abs(sorted_y[3] - sorted_y[0])):
            return [sorted_x[1], sorted_y[1], sorted_x[2], sorted_y[2]]

    @staticmethod
    def getPoints(node, size):
        return [point for point in node.points if AABBHelper.containsPoint(size, point.x, point.y)]

    @staticmethod
    def pairwise(t):
        it = iter(t)
        return izip(it, it)


class Node(object):
    def __init__(self, size, parent=None):
        self.parent = parent
        self.children = None
        self.points = []
        self.size = size

    def addChildren(self, children):
        if not self.children:
            self.children = children

    def addParent(self, parent):
        self.parent = parent

    def addPoint(self, point):
        self.points.append(point)

    def addPoints(self, points):
        self.points.extend([point for point in points if point not in self.points])


class QuadTree(object):
    """ *Usage Note*: QuadTree not copies postal codes, it consumes codes from container and spreads it inside. """

    maxNodeSize = (-32768, -32768, 32767, 32767)

    def __init__(self, allCodes, cellPostalCodesNum):
        self._allPostalCodes = PostalCodesContainer(allCodes, self.maxNodeSize)
        self._mainNode = Node(self._allPostalCodes.maxNodeSize)
        self._iterator = self._allPostalCodes.allCodes
        self.allNodes = []

        if cellPostalCodesNum <= 1:
            raise ValueError("Must be more than 1 postal code point for Node")
        self._cellPostalCodesNum = cellPostalCodesNum  # each cell should contain a configurable number of postal codes

        self._createTree(self._mainNode)  # constructs the network of nodes (subdivides)

    @staticmethod
    def _containsPoint(node, *args):
        return AABBHelper.containsPoint(node.size, *args) and node.points

    @staticmethod
    def _prepareResult(result):
        for nodeResultList in result:
            for node, result in AABBHelper.pairwise(nodeResultList):
                yield node, result

    @staticmethod
    def _pointsGetter(node, conditionState, *args):
        return node.points

    @staticmethod
    def _closestPostalCode(node, conditionState, *args):
        x, y = args
        pointDeltas = {}
        for point in node.points:
            value = sqrt((x - point.x) ** 2 + (y - point.y) ** 2)
            pointDeltas.setdefault(value, []).append(point)
        if not pointDeltas:
            raise RuntimeError("Empty points on Node - {}".format(node.__dict__))
        return pointDeltas[min(pointDeltas.keys())]

    @staticmethod
    def _generatorsCompare(first, second):
        for point1, point2 in product(first, second):
            if point1 == point2:
                yield point1

    @property
    def allPoints(self):
        return self._resultGetter(getter=self._pointsGetter)

    def addNodes(self, nodes):
        self.allNodes.extend(nodes)

    def removePointsFromIterator(self, points):
        for point in points:
            if point in self._iterator:
                self._iterator.remove(point)

    def _createTree(self, currentMain):
        self.addNodes([currentMain])
        childrenNodes = [Node(size, currentMain) for size in AABBHelper.quadDivide(currentMain.size)]
        points, addNodes = [], False
        for child in childrenNodes:
            counter = 0
            for point in self._iterator:
                if AABBHelper.containsPoint(child.size, point.x, point.y):
                    points.append(point)
                    child.addPoint(point)
                    counter += 1
            if counter >= self._cellPostalCodesNum:
                addNodes = True
                self._createTree(child)  # << Recursive call
        if addNodes:
            currentMain.addChildren(childrenNodes)
            self.addNodes(childrenNodes)
        else:
            currentMain.addPoints(points)
        self.removePointsFromIterator(points)

    def _walk(self, nodes, condition=lambda *args: True, *args):
        for node in nodes:
            conditionResult = condition(node, *args)
            if conditionResult:
                if node.children:
                    yield chain(*self._walk(node.children, condition, *args))   # << Recursive call
                else:
                    yield node, conditionResult

    def _resultGetter(self, finder=lambda *args: True, findArgs=(),
                      getter=lambda node, conditionResult, *args: [node], getterArgs=()):
        result = self._walk([self._mainNode], finder, *findArgs)
        for node, conditionState in self._prepareResult(result=result):
            for result in getter(node, conditionState, *getterArgs):
                yield result

    def findClosestPostalCode(self, x, y):
        return self._resultGetter(finder=self._containsPoint, findArgs=(x, y),
                                  getter=self._closestPostalCode, getterArgs=(x, y))

    def findPointsInBox(self, size):
        return self._resultGetter(finder=AABBHelper.getIntersection, findArgs=(Node(size), ),
                                  getter=AABBHelper.getPoints)

    def __iter__(self):
        return self.allPoints

    def next(self):  # Python 3: def __next__(self)
        return next(self.allPoints)

    def findPostalCodesInBothQuadTrees(self, otherQuadTree):
        """ For given another quadtree, returns all the postal codes stored in both. """
        return self._generatorsCompare(self, otherQuadTree)


class Viewer(object):
    def __init__(self, tree):
        self.tree = tree

        self._plotter = plt
        self._patches = self._getPatches()
        self._colors = self._getColors()
        self._createFigure()
        self._drawPoint()

    def run(self):
        """ Public method: plots you a graph with poligons. """
        self._plotter.show()

    def _getPatches(self):
        return [Polygon(self._getPolygonPoints(node.size), True) for node in tree.allNodes]

    def _getColors(self):
        colors = set()
        while len(colors) != len(self._patches):
            colors.add(100 * random.randint(0, len(self._patches)))
        return list(colors)

    @staticmethod
    def _getPolygonPoints(rect):
        x0, y0, x1, y1 = rect
        return [(x0, y0), (x0, y1), (x1, y1), (x1, y0)]

    def _createFigure(self):
        fig, ax = self._plotter.subplots()
        pObj = PatchCollection(self._patches, cmap=matplotlib.cm.jet, alpha=0.4)
        pObj.set_array(np.array(self._colors))
        ax.add_collection(pObj)

    def _drawPoint(self):
        xLine, yLine = [], []
        for pointObj in self.tree.allPoints:
            xLine.append(pointObj.x)
            yLine.append(pointObj.y)
        self._plotter.scatter(xLine, yLine, marker='x')


if __name__ == "__main__":
    # import sys
    # sys.setrecursionlimit(10 * sys.getrecursionlimit())

    POSTAL_CODES_AMOUNT = 100
    EACH_NODE_POSTAL_CODES_CAPACITY = 3  # each cell should contain a configurable number of postal codes


    def generateRandCodes(amount):
        return (PostalCode("PostalCode_%s" % n,
                           random.randint(QuadTree.maxNodeSize[0] + 30000, QuadTree.maxNodeSize[2] - + 30000),
                           random.randint(QuadTree.maxNodeSize[1] + 30000, QuadTree.maxNodeSize[3] - + 30000))
                for n in range(amount))

    # def generateRandCodes(u):
    #     from math import sin
    #     return (PostalCode('Points', x, sin(x / 12000.0) * 30000.0) for x in range(-32768, 32767, 100))

    points1 = list(generateRandCodes(POSTAL_CODES_AMOUNT))
    points2 = deepcopy(points1)

    tree = QuadTree(points1, EACH_NODE_POSTAL_CODES_CAPACITY)

    """
    For given X/Y coordinates, returns the postal code with the closest center,
    returns list of codes because theoretically there could be several codes with same distance to center.
    """
    samePoint = PostalCode('Find', 1000, 3000)
    # postalCodes contains list of points because we can have symmetric points
    postalCodes = [point for point in tree.findClosestPostalCode(samePoint.x + 1, samePoint.y - 1)]
    print 'findClosestPostalCode: {}'.format(postalCodes)

    """
    For given a bounding box, returns all the postal codes whose centers are included in that bounding box.
    """
    postalCodes = tree.findPointsInBox((QuadTree.maxNodeSize[0] / 2,
                                        QuadTree.maxNodeSize[1] / 2,
                                        QuadTree.maxNodeSize[2] / 2,
                                        QuadTree.maxNodeSize[3] / 2))
    print "findPostalCodesInBox: {}".format(pformat(postalCodes))

    tree2 = QuadTree(points2[:2], EACH_NODE_POSTAL_CODES_CAPACITY)
    for code in tree.findPostalCodesInBothQuadTrees(tree2):
        print 'findPostalCodesInBothQuadTrees: {}'.format(code)

    """ Example of iteration through the stored postal codes in a stable order."""
    for postalCode in tree:
        print 'postal code instance object {}'.format(postalCode)

    Viewer(tree).run()
