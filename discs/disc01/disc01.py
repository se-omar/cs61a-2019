# Alfonso will only wear a jacket outside if it is below 60 degrees or it is raining.
# Write a function that takes in the current temperature and a boolean value telling
# if it is raining and returns True if Alfonso will wear a jacket and False otherwise.
# First, try solving this problem using an if statement.
def wears_jacket_with_if(temp, raining):
    """
    >>> wears_jacket(90, False)
    False
    >>> wears_jacket(40, False)
    True
    >>> wears_jacket(100, True)
    True
    """
    return raining or temp<60

# Write a function that returns True if a positive integer n is a prime number and
# False otherwise.
# Hint: use the % operator: x % y returns the remainder of x when divided by y.


def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    iter = 2
    while iter < n:
        if n % iter == 0:
            return False
        iter += 1
    return True


print(is_prime(251))
