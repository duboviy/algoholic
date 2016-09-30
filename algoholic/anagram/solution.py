"""
Task name: Anagram
Task description: Given two strings s and t, write a function to determine if t is an anagram of s.
Details: https://leetcode.com/problems/valid-anagram/ or README.md in curdir.
"""
from collections import Counter


def trivial_solution(s, t):
    """
    # Time:  O(n*log(n))
    # Space: O(n)
    """
    return sorted(s) == sorted(t)


def optimized_solution(s, t):
    """
    # Time:  O(n)
    # Space: O(1)
    """
    s_counter, t_counter = Counter(s), Counter(t)
    for ch, count in s_counter.iteritems():
        if s_counter[ch] != t_counter[ch]:
            return False

    return len(s) == len(t)


