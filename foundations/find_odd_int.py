"""Foundations Problems from CodeWars.

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.
"""

# My solution:
def find_it(seq):
    """Finds the int that appears an odd number of times in a list (only one will appear odd.)"""

    num_in_seq = set()
    l_nums = {}

    for item in seq:
        num_in_seq.add(item)

        if item in l_nums:
            l_nums[item] += 1
        else:
            l_nums[item] = 1

    for num in num_in_seq:
        if l_nums[num] % 2 != 0:
            return num


# Alternate answer
def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i