# 1.1 Write a function that takes two numbers m and n and returns their product.
# Assume m and n are positive integers. Use recursion, not mul or *!
# Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1.
# For the base case, what is the simplest possible input for multiply?
# For the recursive case, what does calling multiply(m - 1, n) do? What
# does calling multiply(m, n - 1) do? Do we prefer one over the other?
def multiply(m, n):
    if n == 1:
        return m
    return m + multiply(m, n - 1)

print(multiply(5, 3))


# In discussion 1, we implemented the function is prime, which takes in a
# positive integer and returns whether or not that integer is prime, iteratively.
# Now, let’s implement it recursively! As a reminder, an integer is considered
# prime if it has exactly two unique factors: 1 and itself.

def is_prime(n):
    def count_fact(n, i):
        if n == i:
            return 1
        if n % i == 0:
            return 1 + count_fact(n, i + 1)
        return count_fact(n, i + 1)

    return count_fact(n, 1) == 2
    

# Define a function make fn repeater which takes in a one-argument function
# f and an integer x. It should return another function which takes in one
# argument, another integer. This function returns the result of applying f to
# x this number of times.
# Make sure to use recursion in your solution.
def make_func_repeater(f, x):
    def repeat(n):
        if n == 1:
            return f(x)
        return f(repeat(n - 1))
    return repeat


# You want to go up a flight of stairs that has n steps. You can either take 1
# or 2 steps each time. How many different ways can you go up this flight of
# stairs? Write a function count_stair_ways that solves this problem. Assume
# n is positive.
# Before we start, what’s the base case for this question? What is the simplest
# input?
# What do count_stair_ways(n - 1) and count_stair_ways(n - 2) represent?
# Use those two recursive calls to write the recursive case:
def count_stair_ways(n):
    if n == 1 or n == 2:
        return n
    return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    


# Consider a special version of the count_stairways problem, where instead
# of taking 1 or 2 steps, we are able to take up to and including k steps at
# a time.
# Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.
def count_k(n, k):
"""
>>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
4
>>> count_k(4, 4)
8
>>> count_k(10, 3)
274
>>> count_k(300, 1) # Only one step at a time
1
"""



