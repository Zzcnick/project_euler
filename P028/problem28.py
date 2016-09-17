current  = 1
accepted = 0
layer    = 1
total    = 1

while layer < 501:
    if accepted == 4:
        layer += 1
        accepted = 0
    else:
        current += layer * 2
        total += current
        accepted += 1
print total
