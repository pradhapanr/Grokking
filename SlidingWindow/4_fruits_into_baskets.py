"""
You are visiting a farm to collect fruits. The farm has a single row of fruit trees. You will be given two
baskets, and your goal is to pick as many fruits as possible to be placed in the given baskets.

You will be given an array of characters where each character represents a fruit tree. The farm has
following restrictions:

1. Each basket can have only one type of fruit. There is no limit to how many fruit a basket can hold.
2. You can start with any tree, but you can’t skip a tree once you have started.
3. You will pick exactly one fruit from every tree until you cannot, i.e., you will stop when you have to
pick from a third fruit type.

Write a function to return the maximum number of fruits in both baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit = ['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. This can be done if we
start with the second letter: ['B', 'C', 'B', 'B', 'C']

Solution:
Pretty much the exact same as longest substring with k distinct characters, but instead our value
k is set as 2.

Create a map that has the key as a letter and the value is how many times it's appeared in the substring.
Iterate over the whole string expanding the window as you go. If the letter map contains more than 2
keys, then shrink the window until it is equal to 2 again. Store the max length of the substring and
return.
"""


def func(fruits):
    fruit_map = {}
    window_start = 0
    max_fruits = 0

    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        if right_fruit in fruit_map:
            fruit_map[right_fruit] += 1
        else:
            fruit_map[right_fruit] = 1

        while len(fruit_map) > 2:
            left_fruit = fruits[window_start]
            fruit_map[left_fruit] -= 1
            if fruit_map[left_fruit] == 0:
                fruit_map.pop(left_fruit)
            window_start += 1
        max_fruits = max(max_fruits, window_end - window_start + 1)
    return max_fruits


def test_cases():
    case_one = func(fruits=["A", "B", "C", "A", "C"])
    case_two = func(fruits=["A", "B", "C", "B", "B", "C"])

    assert case_one == 3
    assert case_two == 5
