def fib(n):
    prev = 0
    curr = 1
    count = 2
    while count < n:
        # prev, prevprev = prev + prevprev, prev
        temp = curr
        curr = curr + prev
        prev = temp
        count += 1
    return curr


print(fib(8))
