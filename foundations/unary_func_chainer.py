"""Fundamental Problems from CodeWars.
Unary Function Chainer

Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

chained([a,b,c,d])(input)
Should yield the same result as

d(c(b(a(input))))


Example Tests:
def f1(x): return x*2
def f2(x): return x+2
def f3(x): return x**2

def f4(x): return x.split()
def f5(xs): return [x[::-1].title() for x in xs]
def f6(xs): return "_".join(xs)


test.assert_equals( chained([f1,f2,f3])(0), 4 )
test.assert_equals( chained([f1,f2,f3])(2), 36 )
test.assert_equals( chained([f3,f2,f1])(2), 12 )

test.assert_equals( chained([f4,f5,f6])("lorem ipsum dolor"), "Merol_Muspi_Rolod")
"""

# My solution:
def chained(functions):
    """Chains a list of unary functions, and runs them in order. chained([a,b,c,d])(input) would be run as d(c(b(a(input))))."""
    def apply(param):
        """Inner function to chained."""
        result = param
        for function in functions:
            result = function(result)
        return result
    return apply



# Alternative answer
def chained(functions):
    def f(x):
        for function in functions:
            x = function(x)
        return x
    return f


# Alternative answer
def chained(functions):
    return lambda x: reduce(lambda v, f: f(v), functions, x)

