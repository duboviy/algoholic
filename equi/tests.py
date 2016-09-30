""" Module with solution's unit tests. """
import unittest
import inspect
import sys
from pprint import pformat

import solution
from utils.testing import TestData

# my PyPI library =) See https://github.com/duboviy/pybenchmark for details
from pybenchmark import profile, stats, kpystones


class MySolutionTestCase(unittest.TestCase):

    def testTaskDescriptionExample(self):
        """ Test from the task description """
        self.data = TestData([-1, 3, -4, 5, 1, -6, 2, 1], [1, 3, 7])
        self.runTest()

    def testSimplePositive(self):
        """ Test with simple positive left & right side """
        self.data = TestData([1, 3, 1], [1])
        self.runTest()

    def testSimpleNegative(self):
        """ Test with simple negative left & right side """
        self.data = TestData([-1, 3, -1], [1])
        self.runTest()

    def testExtremelyPositiveLargeNumbersPositive(self):
        self.data = TestData([sys.maxint, sys.maxint, sys.maxint], [1])
        self.runTest()

    def testExtremelyNegativeLargeNumbersNegative(self):
        self.data = TestData([-sys.maxint, -sys.maxint, -sys.maxint], [1])
        self.runTest()

    def testExtremelyPositiveLargeNumbersPositiveOverflowTest(self):
        expectedEquiK = 1000
        self.data = TestData(expectedEquiK * [sys.maxint] + [0] + expectedEquiK * [sys.maxint], [expectedEquiK])
        self.runTest()

    def testExtremelyNegativeLargeNumbersNegativeOverflowTest(self):
        expectedEquiK = 1000
        self.data = TestData(expectedEquiK * [-sys.maxint] + [0] + expectedEquiK * [-sys.maxint], [expectedEquiK])
        self.runTest()

    def testOneLargeNumberAtTheEnd(self):
        """ One large number at the end of the sequence. """
        self.data = TestData([0, -sys.maxint, 0, -sys.maxint, sys.maxint], [1])
        self.runTest()

    def testSequenceSum0(self):
        self.data = TestData([0, 0, 0], [0, 1, 2])
        self.runTest()

    def testSingleNumber(self):
        self.data = TestData([5], [0])
        self.runTest()

    def testEmptyInputArray(self):
        self.data = TestData([], [-1])
        self.runTest()

    def testCombinationsOfThreeValues_negative_1_0_and_positive_1(self):
        self.data = TestData([-1, 0, 1] * 1000, [-1])
        self.runTest()

    def testCombinationsOfThreeValues_negative_1_0_and_positive_2(self):
        self.data = TestData([1, 0, -1] * 1000, [-1])
        self.runTest()

    def testCombinationsOfThreeValues_negative_1_0_and_positive_3(self):
        self.data = TestData([0, 1, -1] * 1000, [n for n in xrange(3000) if n % 3 == 0])
        self.runTest()

    def testCombinationsOfThreeValues_negative_1_0_and_positive_4(self):
        self.data = TestData([0, -1, 1] * 1000, [n for n in xrange(3000) if n % 3 == 0])
        self.runTest()

    def test_small_pyramid(self):
        self.data = TestData([0, 1, 2, 3, -1, 3, 2, 1, 0], [4])
        self.runTest()

    """ Correctness/performance tests """

    def testExtremeMaximalSize(self):
        expectedEquiK, expectedKStonePerformance = 10000, kpystones / 2
        self.data = TestData(expectedEquiK*[5] + [0] + expectedEquiK*[5],
                                  [expectedEquiK], expectedKStonePerformance)
        self.runTest()

    """ Performance tests """

    def testLargeLongSequenceOfOnes(self):
        expectedEquiK, expectedKStonePerformance = 10000, kpystones / 2
        self.data = TestData(expectedEquiK*[1] + [0] + expectedEquiK*[1],
                                  [expectedEquiK], expectedKStonePerformance)
        self.runTest()

    def testLargeLongSequenceOfMinusOnes(self):
        expectedEquiK, expectedKStonePerformance = 10000, kpystones / 2
        self.data = TestData(expectedEquiK*[-1] + [0] + expectedEquiK*[-1],
                                  [expectedEquiK], expectedKStonePerformance)
        self.runTest()

    def testMediumPyramid(self):
        expectedEquiK, expectedKStonePerformance = 100, kpystones / 20
        self.data = TestData([i for i in xrange(expectedEquiK)] + [0] + [i for i in xrange(expectedEquiK, 0, -1)],
                                  [expectedEquiK + 1], expectedKStonePerformance)
        self.runTest()

    def testLargePyramid(self):
        """ Large performance test, O(n^2) solutions should fail. """
        expectedEquiK, expectedKStonePerformance = 1000, kpystones / 2
        self.data = TestData([i for i in xrange(expectedEquiK)] + [0] + [i for i in xrange(expectedEquiK, 0, -1)],
                                  [expectedEquiK + 1], expectedKStonePerformance)

    def testHugePyramid(self):
        """ Large performance test, O(n^2) solutions should fail. """
        expectedEquiK, expectedKStonePerformance = 10000, kpystones
        self.data = TestData([i for i in xrange(expectedEquiK)] + [0] + [i for i in xrange(expectedEquiK, 0, -1)],
                                  [expectedEquiK + 1], expectedKStonePerformance)
        self.runTest()

    def testHugeZerosSequence(self):
        """ Large performance test, O(n^2) solutions should fail. """
        expectedEquiK, expectedKStonePerformance = 10000, kpystones / 2
        self.data = TestData([0 for _ in xrange(expectedEquiK)],
                             [i for i in xrange(expectedEquiK)], expectedKStonePerformance)
        self.runTest()

    def runTest(self):
        gen_funcs = inspect.getmembers(solution, inspect.isgeneratorfunction)
        solutions = [(name, gen) for name, gen in gen_funcs if 'solution' in name]

        for name, gen in solutions:
            self.data.solution = gen
            self.data.actual_result = profile(name)(lambda: list(self.data.solution(self.data.input_data)))()
            self.data.actual_kstones = stats[name]['kstones']

            self.assertEqual(self.data.expected_result, self.data.actual_result, msg=pformat(self.data.__dict__))
            # check that performance is lower than expected UPPER LIMIT of algorithm
            if self.data.expected_kstones:
                self.assertLess(self.data.actual_kstones, self.data.expected_kstones, msg=pformat(self.data.__dict__))


if __name__ == "__main__":
    unittest.main()
