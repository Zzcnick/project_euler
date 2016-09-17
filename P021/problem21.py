import math

def sumDiv(x):
    if x == 0:
        return 0
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
    totals = [(z ** (y + 1) - 1) / (z - 1) for [z, y] in [[z,factors[z]] for z in factors]]
    final = 1
    for i in totals:
        final *= i
    final -= x
    return final

total = 0
for i in range(1,10001):
    if i == sumDiv(sumDiv(i)) and i != sumDiv(i):
        #print i, sumDiv(i)
        total += i
print total
