from link import Link
# 1.2 Write a function that takes a sorted linked list of integers and mutates it so that
# all duplicates are removed.
def remove_duplicates(lnk):
    """
    >>> lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
    >>> remove_duplicates(lnk)
    >>> lnk
    Link(1, Link(5))
    """
    while lnk != Link.empty:
        if lnk.rest is not Link.empty and lnk.first == lnk.rest.first:
            lnk.rest = lnk.rest.rest
        lnk = lnk.rest


lnk = Link(1, Link(1, Link(1, Link(1, Link(5)))))
remove_duplicates(lnk)
print(lnk)
