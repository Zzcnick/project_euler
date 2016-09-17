oof = open("p099_base_exp.txt", "r")
rab = oof.read()
oof.close()
rab = rab.split("\n")
for i in range(len(rab)):
    rab[i] = rab[i].split(",")
line = -1
highest = -1
for i in rab:
    if int(i[0]) ** int(i[1]) > highest:
        highest = int(i[0]) ** int(i[1])
        line = rab.index(i)
        print i
print line
