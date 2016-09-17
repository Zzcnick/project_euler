'''
def fact(x):
    oof = 1
    for i in range(1, x+1):
        oof *= i
    return oof
'''

table = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
def fact(x):
    place = range(0,10).index(x)
    return table[place]

# Both are around the same efficiency.

def sDF(x):
    total = 0
    while x > 0:
        total += fact(x % 10)
        x = x / 10
    return total

start = 3
total = 0
while start < 1000000:
    if start == sDF(start):
        total += start
        print total, start
    start += 1
print total
