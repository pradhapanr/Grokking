"""
Given an array containing 0s and 1s, if you are allowed to replace no more than 'k' 0s with
1s, find the length of the longest contiguous subarray having all 1s.

Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of
1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous
subarray of 1s having length 9.

Solution:
Pretty much the same as the last replacement question. Only thing that changes is that
because there's one character that needs it's frequency tracked, we can eliminate the
use of a hashmap. Rest of the process is the exact same.
"""


def func(arr, k):
    l = 0
    f = 0
    max_len = 0
    for r in range(len(arr)):
        if arr[r] == 1:
            f += 1

        if ((r - l + 1) - f) > k:
            if arr[l] == 1:
                f -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len


def test_cases():
    case_one = func(arr=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2)
    case_two = func(arr=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3)

    assert case_one == 6
    assert case_two == 9
