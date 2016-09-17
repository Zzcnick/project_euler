def sumDigits(x):
    total = 0
    while x > 0:
        total = total + x % 10
        x = x / 10
    return total

print sumDigits(2 ** 1000)
