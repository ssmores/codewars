"""Fundamental Problems from CodeWars.
Sum of two lowest positive integers:
Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 integers. No floats or empty arrays will be passed.

For example, when an array is passed like [19,5,42,2,77], the output should be 7.

[10,343445353,3453445,3453545353453] should return 3453455.

Hint: Do not modify the original array.
"""

# My solution:
def sum_two_smallest_numbers(numbers):
    """Returns sum of two lowest positive ints in array (min array length is 4)."""
    numbers.sort()
    return numbers[0] + numbers[1]


# MY ALTERNATIVE SOLUTION
def sum_two_smallest_numbers(numbers):
    """Returns sum of 2 lowest positive ints in array, not using Python built in sort method."""

    smallest = numbers[0]
    second = numbers[1]

    for num in numbers[2:]:
        if num < smallest:
            smallest = num
        elif num < second:
            second = num

    return smallest + second


# Alternative answer
def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])


# Alternative answer
def sum_two_smallest_numbers(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))
