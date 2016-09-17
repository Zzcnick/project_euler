def name_sum(name):
    total = 0
    for i in name:
        total += ord(i) - 64
    return total

data = open("p022_names.txt", "r")
raw = data.read()
data.close()
cut = raw.replace('''"''', "")
cut = cut.split(",")
new = sorted(cut)
#print new[:100]
total = 0
for i in range(len(new)):
    total += (i + 1) * name_sum(new[i])
print total
