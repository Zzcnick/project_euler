def fact(x):
    oof = 1
    for i in range(1, x+1):
        oof *= i
    return oof

orig    = [str(i) for i in range(1, 10)[::-1]]
numbers = [fact(x) for x in range(1, 10)][::-1]
total = 999999
moves = ''
while True:
    if total >= numbers[0]:
        total -= numbers[0]
        moves += orig[0]
    else:
        numbers = numbers[1:]
        orig = orig[1:]
    if total == 0:
        print moves
        break
print -1

#2783915460
