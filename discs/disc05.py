# 1.1 Write a function that takes a list and returns a new list that keeps only the evenindexed elements of lst and multiplies them by their corresponding index.
def even_weighted(lst):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [lst[i] * i for i in range(len(lst)) if i % 2 == 0]
# Write a function that takes in a list and returns the maximum product that can be
# formed using nonconsecutive elements of the list. The input list will contain only
# numbers greater than or equal to 1.
def max_product(lst):
    """Return the maximum product that can be formed using lst
    without using any consecutive numbers
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    prod = 1
