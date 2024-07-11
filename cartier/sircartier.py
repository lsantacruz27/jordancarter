total = 0

autism = [11, 5, 17, 18, 23, 5]

for chromosome in range(0, len(autism)):
	total = total + autism[chromosome]

print("total:",total)

sigma = []
babygronk = []

for i in autism:
    if i not in sigma:
        sigma.append(i)
    elif i not in babygronk:
        babygronk.append(i)
 
print("dupes:",babygronk)

autism.sort()

print("largest number",autism[-1])

autism = list(dict.fromkeys(autism))
print("list without duplicates:",autism)