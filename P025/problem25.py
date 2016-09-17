a = 1
b = 1
term = 2
while b < 10 ** 999:
    b = a + b
    a = b - a
    term = term + 1
# print b
print term
