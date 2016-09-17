def sumDigits(x):
    total = 0
    while x > 0:
        total = total + x % 10
        x = x / 10
    return total

total = 1
for i in range(1, 101):
    total = total * i
print sumDigits(total)
