"""
Given an array of positive numbers and a positive number 'S', find the length of the
smallest contiguous subarray whose sum is greater than or equal to 'S'. Return 0 if
no such subarray exists.

Example 1:

Input: [2, 1, 5, 2, 3, 2], S=7
Output: 2
Explanation: The smallest subarray with a sum greater than or equal to '7' is [5, 2].
Example 2:

Input: [2, 1, 5, 2, 8], S=7
Output: 1
Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
Example 3:

Input: [3, 4, 1, 1, 6], S=8
Output: 3
Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1]
or [1, 1, 6].

Solution:
Loop over the entire array. Expand window if the sum is >= S. If not, then shrink the
window. Each iteration should track the num of elements in the subarray and store
the max. Return this max value.
"""
import math


def func(arr, s):
    window_start = 0
    min_length = math.inf
    sum = 0
    for window_end in range(len(arr)):
        sum += arr[window_end]

        while sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            sum -= arr[window_start]
            window_start += 1
    if min_length == math.inf:
        return 0
    return min_length


def test_cases():
    case_one = func(arr=[2, 1, 5, 2, 3, 2], s=7)
    case_two = func(arr=[2, 1, 5, 2, 8], s=7)
    case_three = func(arr=[3, 4, 1, 1, 6], s=8)
    case_four = func(arr=[2, 3, 1, 2], s=20)

    assert case_one == 2
    assert case_two == 1
    assert case_three == 3
    assert case_four == 0
