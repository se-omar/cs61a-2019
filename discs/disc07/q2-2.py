# 2.2 Write the function is palindrome such that it works for any data type that implements the sequence interface.
# Assume that the Link class has implemented the \_\_len\_\_ method and a \_\
# _getitem\_\_ method which takes in integers.

import math

def is_palindrome(seq):
    """ Returns True if the sequence is a palindrome. A palindrome is a sequence
    that reads the same forwards as backwards
    >>> is_palindrome(Link("l", Link("i", Link("n", Link("k")))))
    False
    >>> is_palindrome(["l", "i", "n", "k"])
    False
    >>> is_palindrome("link")
    False
    >>> is_palindrome(Link.empty)
    True
    >>> is_palindrome([])
    True
    >>> is_palindrome("")
    True
    >>> is_palindrome(Link("a", Link("v", Link("a"))))
    True
    >>> is_palindrome(["a", "v", "a"])
    True
    >>> is_palindrome("ava")
    True
    """
    if len(seq) % 2 == 0:
        for i in range(len(seq)):
            if seq[i] != seq[len(seq) - (i+1)]:
                return False
        return True

    else:
        mid = math.ceil(len(seq) / 2) - 1
        
        for i in range(len(seq)):
            if i == mid:
                return True
            if seq[i] != seq[len(seq) - (i+1)]:
                return False
