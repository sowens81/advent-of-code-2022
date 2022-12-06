from collections import Counter

x=1
y=0
z=0
elfs={}

file = open("data.txt")
lines = file.readlines()

for line in lines:
    l = line.strip()
    if len(l) > 0:
        y += int(l)
    
    elif len(l) == 0:
        elf= "elf-" + str(x)
        elfs[elf] = y
        x += 1
        y = 0

file.close()

k = Counter(elfs)
high = k.most_common(3)
for i in high:
    value=i[1]
    z += value

print(z)