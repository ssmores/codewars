"""Foundations Problems from CodeWars.

Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters, - each taken only once - coming from s1 or s2.

Examples:

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

# My solution:
def longest(s1, s2):
    """Takes 2 strings (only lowers), and returns longest, sorted string, of only distinct letters."""
    dist_l = set()
    new_s = s1 + s2
    
    for l in new_s:
        dist_l.add(l)

    dist_letters = []
    for let in dist_l:
        dist_letters.append(let)

    dist_letters.sort()

    output = ''
    for item in dist_letters:
        output += item

    return output


# Alternative answer
def longest(s1, s2):
    return ''.join(sorted((set(s1+s2))))