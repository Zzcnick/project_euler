'''
n = 1
def f(x):
    return n % x
while sum(map(f, [16, 9, 5, 7, 11, 13, 17, 19])) != 0:
    n = n + 1
print n
'''
# "Works", but not really. Inefficient.
print 16 * 9 * 5 * 7 * 11 * 13 * 17 * 19
