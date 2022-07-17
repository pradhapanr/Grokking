"""
Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters
with any letter, find the length of the longest substring having the same letters after replacement.

Example 1:
Input: String="aabccbb", k=2
Output: 5
Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".

Example 2:
Input: String="abbcb", k=1
Output: 4
Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".

Example 3:
Input: String="abccde", k=1
Output: 3
Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".

Solution:
VERY TRICKY QUESTION. SHOULD REALLY THINK WITH STUFF LIKE THIS. LOTS OF OPTIMIZATIONS.

In this question, what determines if a substring is valid or not is if it contains enough
repeating characters such that the excess characters can be covered by the k replacements.
This means that your condition to shrink your substring should be (len(substr) - num_repeats).
Create a variable to store the max number of repeating characters. As you iterate over the
string, each new character should be checked to see if it now contains the max number of
repeating characters in your substring. If it does, then that becomes the new maximum.
As you shrink your substring, you DO NOT need to update the maximum number of repeating
characters. Even though it may be technically incorrect for your current substring, the
only strings you are actually looking for are ones with THAT many repeating characters
so anything else will never be of the maximum length. This also means you do not need
to shrink your substring smaller than what the previous size was, you just need to
remove the character at the windows start to continue searching. If it's an invalid
substring, it will never grow, it will just shift over one index.

An alternate solution is to constantly check for the max frequency by getting the max
of the values in the dictionary. This way, you can loop again and shrink until your
window contains a valid substring. But as stated before, this is not necessary.
"""


def func(string, k):
    window_start = 0
    max_f = 0
    max_length = 0
    char_map = {}
    for window_end in range(len(string)):
        right_char = string[window_end]
        if right_char in char_map:
            char_map[right_char] += 1
        else:
            char_map[right_char] = 1

        max_f = max(max_f, char_map[right_char])

        if ((window_end - window_start + 1) - max_f > k):
            char_map[string[window_start]] -= 1
            window_start += 1
        max_length = max(max_length, window_end - window_start + 1)
    return max_length


def test_cases():
    case_one = func(string="aabccbb", k=2)
    case_two = func(string="abbcb", k=1)
    case_three = func(string="abccde", k=1)

    assert case_one == 5
    assert case_two == 4
    assert case_three == 3
