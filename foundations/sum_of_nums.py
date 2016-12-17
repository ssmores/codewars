"""Foundations Problems from CodeWars.
Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!

Example: 
get_sum(1, 0) == 1   // 1 + 0 = 1
get_sum(1, 2) == 3   // 1 + 2 = 3
get_sum(0, 1) == 1   // 0 + 1 = 1
get_sum(1, 1) == 1   // 1 Since both are same
get_sum(-1, 0) == -1 // -1 + 0 = -1
get_sum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2
"""

# My solution:
def get_sum(a,b):
    """FInd sum of all numbers between two integers (not ordered). Return number if inputs are equal."""
    if a == b:
        return a
    
    total = 0
    if a < b:
        for num in range(a, b + 1):
            total += num
    else:
        for num in range(b, a + 1):
            total += num

    return total


# Alternative answer
def get_sum(a,b):
    return sum(xrange(min(a,b), max(a,b)+1))


# Alternative answer
def get_sum(a,b):
    return sum(range(min(a, b), max(a, b) + 1))