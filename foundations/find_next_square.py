"""Foundations Problems from CodeWars.

You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral perfect square after the one passed as a parameter. Recall that an integral perfect square is an integer n such that sqrt(n) is also an integer.

If the parameter is itself not a perfect square, than -1 should be returned. You may assume the parameter is positive.

Examples:

findNextSquare(121) --> returns 144
findNextSquare(625) --> returns 676
findNextSquare(114) --> returns -1 since 114 is not a perfect

"""

# My solution:
from math import sqrt

def find_next_square(sq):
    """Return the next square if sq is a square, -1 otherwise."""

    sq_num = int(sqrt(sq))
    if sq_num ** 2 == sq:
        return (sq_num + 1) ** 2

    return -1


# Alternative answer
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1


# Alternate answer
def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    i = 1
    temp = sq
    while temp > 0: # a perfect square must be a sum of a arithmetic sequence by 2
        temp -= i
        i +=2
    if temp == 0:
        return sq + i
    else:
        return -1
