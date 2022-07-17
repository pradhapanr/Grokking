"""
Problem Description

Given an array of positive numbers and a positive number 'k,' find the maximum sum of any
contiguous subarray of size 'k'.

Example 1:
Input: [2, 1, 5, 1, 3, 2], k=3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
Input: [2, 3, 4, 1, 5], k=2
Output: 7
Explanation: Subarray with maximum sum is [3, 4].

Solution:
First, initialize your subarray sum with the first k digits. Then, we can also keep track
of the largest subarray sum from here. Start a loop which goes from the beginning of the
array to the length - k so we don't reach out of bounds. Then we subtract the first index
of the subaray from the sum and add the next. Then compare our previous largest sum to
our now sum and overwrite if current sum is larger.

We don't need to explicitly track window start and end because the size of the window
is constant. Therefore, we can just subtract and add the values relative to the subarray
size.
"""


def func(arr, k):
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    max_sum = curr_sum
    for i in range(len(arr) - k):
        curr_sum -= arr[i]
        curr_sum += arr[i + k]
        max_sum = max(max_sum, curr_sum)
    return max_sum


def test_cases():
    case_one = func(arr=[2, 1, 5, 1, 3, 2], k=3)
    case_two = func(arr=[2, 3, 4, 1, 5], k=2)

    assert case_one == 9
    assert case_two == 7
