number = "."
count = 1
while len(number) < 1000001:
    number += str(count)
    count += 1
print int(number[1]) * int(number[10]) * int(number[100]) * int(number[1000]) * int(number[10000]) * int(number[100000]) * int(number[1000000])



