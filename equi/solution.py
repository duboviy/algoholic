"""
Task name: Equilibrium
Task description: Find an index in an array such that its prefix sum equals its suffix sum.
Details: https://codility.com/demo/results/demo8GXXQA-FDP/#task-0 or README.md in curdir.
"""


def trivial_solution(array):
    """ Time complexity: O(n**2). """
    yielded = False

    for i, _ in enumerate(array):
        if sum(array[0:i]) == sum(array[i+1:]):
            yielded = True
            yield i

    if yielded is False:
        yield -1


def optimized_solution_1(array):
    """ Time complexity: O(2n) -> O(n). """
    sum_total = sum(array)
    sum_left = 0
    yielded = False

    for i, v in enumerate(array):
        sum_right = sum_total - sum_left - v

        if sum_right == sum_left:
            yielded = True
            yield i

        sum_left += v

    if yielded is False:
        yield -1


def optimized_solution_2(a):
    """ Time complexity: O(2n) -> O(n). """
    sum_right = sum(a)
    sum_left = 0
    yielded = False

    for index,value in enumerate(a):
        sum_right -= value

        if sum_left == sum_right:
            yielded = True
            yield index

        sum_left += value

    if yielded is False:
        yield -1
