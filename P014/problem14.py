def collatz(n):
    length = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            length += 1
        else:
            n = 3 * n + 1
            length += 1
    return length

number = 0
length = 0
for i in range(1, 1000000):
    if collatz(i) > length:
        number = i
        length = collatz(i)
print number
