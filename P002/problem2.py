a = 1
b = 1
tmp = 0
while b <= 4000000:
    if b % 2 == 0:
        tmp = tmp + b
    b = b + a
    a = b - a
print tmp
