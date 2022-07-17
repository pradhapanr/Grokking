"""
Given a string, find the length of the longest substring, which has all distinct characters.

Example 1:
Input: String="aabccbb"
Output: 3
Explanation: The longest substring with distinct characters is "abc".

Example 2:
Input: String="abbbb"
Output: 2
Explanation: The longest substring with distinct characters is "ab".

Example 3:
Input: String="abccde"
Output: 3
Explanation: Longest substrings with distinct characters are "abc" & "cde".

Solution:
Create a hashmap that stores characters as well as their last seen index in the window.
As you iterate over the string you can consistently update this map with the most recent
index. This way, if you expand your sliding window and take in a duplicate character, you
can "jump" the start of the window to the index that makes the substring valid again.
To avoid weird edgecases where the last seen index may be from a previous substring, you
can max this value with the current start of the window. Now the question proceeds like a
classic longest substring problem.
"""


def func(string):
    char_index_map = {}
    l = 0
    max_len = 0

    for r in range(len(string)):
        r_char = string[r]
        if r_char in char_index_map:
            # max with window start to prevent us from jumping back from old index values
            l = max(l, char_index_map[r_char] + 1)
        char_index_map[r_char] = r
        max_len = max(max_len, r - l + 1)
    return max_len


def test_cases():
    case_one = func("aabccbb")
    case_two = func("abbbb")
    case_three = func("abccde")

    assert case_one == 3
    assert case_two == 2
    assert case_three == 3
