"""Foundations Problems from CodeWars.

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.

For example:

 persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 persistence(4) => 0   # Because 4 is already a one-digit number
 """

 # My solution
 def persistence(n):
    """Multiplies each number in n until n is a single digit. Returns how many iterations this takes."""

    count = 0

    while n > 9:
        n = str(n)
        temp = 1
        for num in n:
            temp = temp * int(num)
        count += 1
        n = temp

    return count


# Alternative answer which didn't use lambdas
def persistence(n):
    x = list(str(n))
    c = 0
    while len(x) > 1:
        m = 1
        for i in x:
            m *= int(i)
        x = list(str(m))
        c += 1
    return c

    
