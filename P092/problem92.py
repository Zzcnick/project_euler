def squareSumDigits(x):
    total = 0
    while x > 0:
        total = total + (x % 10) ** 2
        x = x / 10
    return total

def test(x):
    if x == 89:
        return True
    if x == 1:
        return False
    return test(squareSumDigits(x))

count = 0
x = 1
while x < 10000000:
    if test(x):
        count += 1
    x += 1
print count
