"""Foundations Problems from CodeWars.

Can you find the needle in the haystack?

Write a function findNeedle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle

So

find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk'])
should return

'found the needle at position 5'
"""

# My solution:
def find_needle(haystack):
    """Finds sting 'needle' in a list. Returns a statement at which index the string is."""

    index = None
    for i, item in enumerate(haystack):
        if item == 'needle':
            index = i

    return 'found the needle at position {}'.format(index)


# My solution slightly refactored. 
def find_needle(haystack):
    """Finds string 'needle' in a list. Returns statement at which index 'needle' is found."""

    for i, item in enumerate(haystack):
        if item == 'needle':
            return 'found the needle at position {}'.format(i)


# MY ALTERNATIVE SOLUTION
def find_needle(haystack):
    """Finds sting 'needle' in a list. Returns a statement at which index the string is."""

    index = None
    for i in range(len(haystack)):
        if haystack[i] == 'needle':
            index = i

    return 'found the needle at position {}'.format(index)            


# Alternative answer
def find_needle(haystack):
    return 'found the needle at position {}'.format(haystack.index('needle'))


