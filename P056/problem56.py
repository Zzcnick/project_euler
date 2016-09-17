def sumDigits(x):
    total = 0
    while x > 0:
        total = total + x % 10
        x = x / 10
    return total

high = 0
for a in range(1, 100):
    for b in range(1, 100):
        if sumDigits(a ** b) > high:
            high = sumDigits(a ** b)
print high
