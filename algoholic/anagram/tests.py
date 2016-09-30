""" Module with solution's unit tests. """
import unittest
import inspect
from pprint import pformat
from string import lowercase
from random import choice

import solution
from utils.testing import TestData

# my PyPI library =) See https://github.com/duboviy/pybenchmark for details
from pybenchmark import profile, stats, kpystones


class MySolutionTestCase(unittest.TestCase):

    def testTaskDescriptionExample(self):
        """ Test from the task description """
        self.data = TestData(["anagram", "nagaram"], True)
        self.runTest()

    def testSimplePositive1(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["rac", "car"], True)
        self.runTest()

    def testSimplePositive2(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["nl", "ln"], True)
        self.runTest()

    def testSimplePositive3(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["cx", "xc"], True)
        self.runTest()

    def testSimpleNegative1(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["rat", "car"], False)
        self.runTest()

    def testSimpleNegative2(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["rat", "cara"], False)
        self.runTest()

    def testSimpleNegative3(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["rat", "carr"], False)
        self.runTest()

    def testOneCharStr(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["c", "c"], True)
        self.runTest()

    def testEmptyStr(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["", ""], True)
        self.runTest()

    def testNegativeWithEmptyStr1(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["a", ""], False)
        self.runTest()

    def testNegativeWithEmptyStr2(self):
        """ Test with simple positive left & right side """
        self.data = TestData(["", "a"], False)
        self.runTest()

    """ Performance tests """

    def testExtremeBigStrSize(self):
        expectedStrsK = 10000
        expectedStrs = [lowercase * expectedStrsK, lowercase * expectedStrsK]
        expectedKStonePerformance = kpystones / 9
        self.data = TestData(expectedStrs, True, expectedKStonePerformance)
        self.runTest()

    def testExtremeBigStrSizeNegative(self):
        expectedStrsK = 1000000
        expectedStrs = [(choice(lowercase) * expectedStrsK) + 'a', choice(lowercase) * expectedStrsK]
        expectedKStonePerformance = kpystones
        self.data = TestData(expectedStrs, False, expectedKStonePerformance)
        self.runTest()

    def runTest(self):
        funcs = inspect.getmembers(solution, inspect.isfunction)
        solutions = [(name, f) for name, f in funcs if 'solution' in name]

        for name, f in solutions:
            self.data.solution = f
            self.data.actual_result = profile(name)(lambda: self.data.solution(*self.data.input_data))()
            self.data.actual_kstones = stats[name]['kstones']

            self.assertEqual(self.data.expected_result, self.data.actual_result, msg=pformat(self.data.__dict__))
            # check that performance is lower than expected UPPER LIMIT of algorithm
            if self.data.expected_kstones:
                self.assertLess(self.data.actual_kstones, self.data.expected_kstones, msg=pformat(self.data.__dict__))


if __name__ == "__main__":
    unittest.main()
