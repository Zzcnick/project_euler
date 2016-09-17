def fact(x):
    oof = 1
    for i in range(1, x+1):
        oof *= i
    return oof

count = 0
for c in range(23, 101):
    for r in range(0, c):
        if fact(c) / (fact(r) * fact(c - r)) > 1000000:
            count += 1
print count
