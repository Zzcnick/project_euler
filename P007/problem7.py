def is_prime(n):
    limit = n ** 0.5
    check = 2
    while check <= limit:
        if n % check == 0:
            return False
        check = check + 1
    return True

n = 2
count = 0
while count < 10000:
    n = n + 1
    if is_prime(n):
        count = count + 1
print n

# Strange, 10001th number requries < 10000.
