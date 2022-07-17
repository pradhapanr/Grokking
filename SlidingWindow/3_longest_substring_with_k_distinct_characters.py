"""
Given a string, find the length of the longest substring in it with no more than K distinct characters.

You can assume that K is less than or equal to the length of the given string.

Example 1:

Input: String="araaci", K=2
Output: 4
Explanation: The longest substring with no more than '2' distinct characters is "araa".
Example 2:

Input: String="araaci", K=1
Output: 2
Explanation: The longest substring with no more than '1' distinct characters is "aa".
Example 3:

Input: String="cbbebi", K=3
Output: 5
Explanation: The longest substrings with no more than '3' distinct characters are "cbbeb" & "bbebi".

Solution:
Create a map that has the key as a letter and the value is how many times it's appeared in the substring.
Iterate over the whole string expanding the window as you go. If the letter map contains more than K
keys, then shrink the window until it is equal to K again. Store the max length of the substring and
return.
"""


def func(string, k):
    char_map = {}
    l = 0

    max_len = 0
    for r in range(len(string)):
        r_char = string[r]
        char_map[r_char] = 1 + char_map.get(r_char, 0)
        while len(char_map) > k:
            l_char = string[l]
            char_map[l_char] -= 1
            if char_map[l_char] == 0:
                char_map.pop(l_char)
            l += 1
        max_len = max(max_len, r - l + 1)

    return max_len


def test_cases():
    case_one = func(string="araaci", k=2)
    case_two = func(string="araaci", k=1)
    case_three = func(string="cbbebi", k=3)

    assert case_one == 4
    assert case_two == 2
    assert case_three == 5
