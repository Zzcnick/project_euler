import math

def numDiv(x):
    num = x
    factors = {}
    test = 2
    while test <= math.sqrt(num):
        if num % test == 0:
            if test in factors:
                factors[test] += 1
            else:
                factors[test] = 1
            num /= test
            test = 2
        else:
            test += 1
    if num != 1:
        if num in factors:
            factors[num] += 1
        else:
            factors[num] = 1
    total = 1
    for i in [factors.get(x) + 1 for x in factors]:
        total *= i
    return total

inc = 2
start = 1
while numDiv(start) < 501:
    start += inc
    inc += 1
print start
