# My solution.
def even_or_odd(numbers):
    """Returns True if number is even, False if not."""
    if numbers % 2 == 0:
        return True
    else:
        return False


# This is a ternery operation solution.
def even_or_odd_alt(numbers):
    """Returns True if even, False if not.  Function is using ternery operation."""
    return 'Even' if numbers % 2 == 0 else 'Odd'


# This is another ternery operation solution.
def even_or_odd_3(numbers):
    """Returns True if even, False if not. Function is using ternery operation."""
    return 'Odd' if numbers % 2 else 'Even'

