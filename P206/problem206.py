#19 digits
# 1 _2 _3 _4 _5 _6 _7 _8 _9 00
import math

for i in range(100000007, 320000007, 10):
    a = str(i ** 2)
    if a[0] == '1' and a[2] == '2' and a[4] == '3' and a[6] == '4' and a[8] == '5' and a[10] == '6' and a[12] == '7' and a[14] == '8' and a[16] == '9':
        print a
        break
