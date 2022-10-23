def accumulate(combiner, base, n, term):
    prod = term(n)
    while n > 1:
        prod = combiner(term(n - 1), prod)
        n -= 1

    return combiner(base, prod)

