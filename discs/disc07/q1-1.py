from link import Link
# 1.1 Write a function that takes in a Python list of linked lists and multiplies them
# element-wise. It should return a new linked list.
# If not all of the Link objects are of equal length, return a linked list whose length is
# that of the shortest linked list given. You may assume the Link objects are shallow
# linked lists, and that lst of lnks contains at least one linked list.
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    firsts = 1
    for lnk in lst_of_lnks:
        if lnk is Link.empty:
            return Link(Link.empty)
        firsts *= lnk.first

    lnk_of_rests = [lnk.rest for lnk in lst_of_lnks]
    # for lnk in lst_of_lnks:
    #     lnk_of_rests.append(lnk.rest)

    return Link(firsts, multiply_lnks(lnk_of_rests))


a = Link(2, Link(3, Link(5)))
b = Link(6, Link(4, Link(2)))
c = Link(4, Link(1, Link(0, Link(2))))
p = multiply_lnks([a, b, c])
print(p.first)
print(p.rest.first)
print(p.rest.rest.rest)
