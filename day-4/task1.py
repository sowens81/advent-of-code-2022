errorLines=0

file = open("data.txt")
lines = file.readlines()
pairs = [line.strip() for line in lines]

def validate_range(a, b):
    startA, endA = map(int, a.split('-'))
    startB, endB = map(int, b.split('-'))
    return startB <= startA and endA <= endB

for index, p in enumerate(pairs):
    workingList = []
    a, b = p.split(',')
    print("line:" + str(index+1))
    if validate_range(a, b) or validate_range(b, a):
        print("Bad line:" + str(index+1))
        errorLines += 1
            
print( "There are " + str(errorLines) + " overlapping jobs.")