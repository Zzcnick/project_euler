n = 0
for x in range(100, 1000):
    for y in range (100, 1000):
        test = x * y
        if test > n and str(test) == str(test)[::-1]:
            n = test
print n
