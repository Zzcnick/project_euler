def pSD(x, exp):
    total = 0
    while x > 0:
        total += (x % 10) ** exp
        x /= 10
    return total

total = 0
test = 1
while True:
    test += 1
    if pSD(test, 5) == test:
        total += test
        print total, test

# ends at 194979
