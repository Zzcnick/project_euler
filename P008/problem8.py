def test(string):
    tmp = 1
    for i in range(0, len(string)):
        print int(string[i])
        tmp *= int(string[i])
    print tmp

test('1234')
