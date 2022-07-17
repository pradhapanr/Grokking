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
    letter_map = {}
    window_start = 0

    longest_length = 0
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in letter_map:
            letter_map[right_char] += 1
        else:
            letter_map[right_char] = 1
        while len(letter_map) > k:
            left_char = string[window_start]
            letter_map[left_char] -= 1
            if letter_map[left_char] == 0:
                letter_map.pop(left_char)
            window_start += 1
        longest_length = max(longest_length, window_end - window_start + 1)

    return longest_length


def test_cases():
    case_one = func(string="araaci", k=2)
    case_two = func(string="araaci", k=1)
    case_three = func(string="cbbebi", k=3)

    assert case_one == 4
    assert case_two == 2
    assert case_three == 5
