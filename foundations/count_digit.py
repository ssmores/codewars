"""Fundamental Problems from CodeWars.

Take an integer n (n >= 0) and a digit d (0 <= d <= 9) as an integer. Square all numbers k (0 <= k <= n) between 0 and n. Count the numbers of digits d used in the writing of all the k**2. Call nb_dig (or nbDig or ...) the function taking n and d as parameters and returning this count.

Examples:

n = 10, d = 1, the k*k are 0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100
We are using the digit 1 in 1, 16, 81, 100. The total count is then 4.

nb_dig(25, 1):
the numbers of interest are
1, 4, 9, 10, 11, 12, 13, 14, 19, 21 which squared are 1, 16, 81, 100, 121, 144, 169, 196, 361, 441
so there are 11 digits `1` for the squares of numbers between 0 and 25.
Note that 121 has twice the digit 1.

"""

# My solution:
def nb_dig(n, d):
    """Squares values up to n, provides a count of instances of d in squared values."""

    #Count of d in squares.
    d_in_sq = 0
    for i in range(n + 1):
        # Inner loop looks for instances of d in string of square.
        for ltr in str(i**2):
            # Looks to see if the int of each square character number is the same as d.
            if int(ltr) == d:
                d_in_sq +=1

    return d_in_sq 


# Alternative answer
def nb_dig(n, d):
    return ''.join(str(a ** 2) for a in xrange(n + 1)).count(str(d))


#Alternative answer
def nb_dig(n, d):
    return sum([str(x**2).count(str(d)) for x in range(n+1)])