import time
def is_prime(n):
    limit = n ** 0.5
    check = 2
    while check <= limit:
        if n % check == 0:
            return False
        check = check + 1
    return True

start = time.time()
total = 0
n = 2
while n < 2000000:
    if is_prime(n):
        total = total + n
    n = n + 1
print total
end = time.time()
print "time: ", end - start
