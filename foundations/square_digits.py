"""Foundations Problems from CodeWars.

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
"""

# My solution:
def square_digits(num):
    """Squares every digit in a number, and returns the string of the squared numbers."""

    output = ''
    for digit in str(num):
        s_digit = int(digit) ** 2
        output += str(s_digit)

    return int(output)


# Alternative solution
def square_digits(num):
    ret = ""
    for x in str(num):
        ret += str(int(x)**2)
    return int(ret)