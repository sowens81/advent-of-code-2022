x=1
y=0

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

max_value = max(elfs, key=elfs.get)
print(max_value)
print(elfs.get(max_value))