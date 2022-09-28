# Write curry2 as a lambda function

# original version
def curry2(h):
    def f(x):
        def g(y):
                return h(x, y)
        return g
    return f

# lambda version
curry2 = lambda h: lambda x: lambda y: h(x, y)


# Write a function that takes in a function cond and a number n and prints
# numbers from 1 to n where calling cond on that number returns True.
def keep_ints(n):
    def keep_ints_helper(cond):
        num = n
        while num > 0:
            if cond(num):
                print(num)
            num -= 1
    return keep_ints_helper

# keep_ints(5)(lambda x: x %2 == 0)

# Write a function and add that takes a one-argument function f and a number
# n as arguments. It should return a function that takes one argument, and
# does the same thing as the function f, except also adds n to the result.
def and_add(f, n):
    """Return a new function. This new function takes an
    argument x and returns f(x) + n.
    >>> def square(x):
    ... return x * x
    >>> new_square = and_add(square, 3)
    >>> new_square(4) # 4 * 4 + 3
    19
    """
    def g(x):
        return f(x) + n
    return g