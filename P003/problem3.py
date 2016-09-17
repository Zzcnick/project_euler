def is_prime(n):
    limit = n ** 0.5
    check = 2
    while check <= limit:
        if n % check == 0:
            return False
        check = check + 1
    return True

n = 60085147514312
check = 2
while is_prime(n) == False:
    if n % check == 0:
        n = n / check
        check = 1
    check = check + 1
print n
