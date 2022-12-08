import string
lineCount=0
groupCount=0
badgeGroups=[]
groupList=[]

errorScoring= {}
alphabetLowerCase = list(string.ascii_lowercase)
alphabetUpperCase = list(string.ascii_uppercase)
totalErrorScore=0

for index, a in enumerate(alphabetLowerCase):
    letter=a
    value= index+1
    errorScoring[letter] = value
    
for index, a in enumerate(alphabetUpperCase):
    letter=a
    value= index+27
    errorScoring[letter] = value

file = open("data.txt")
lines = file.readlines()


def find_the_badge(groupList):
    listX = []
    listY = []
    listZ = []
    errors = []
    
    for l in groupList[0]:
        listX.append(l)
    
    for l in groupList[1]:
        listY.append(l)
    
    for l in groupList[2]:
        listZ.append(l)
    
    for x in listX :
        for y in listY:
            if x == y:
                for z in listZ:
                    if y == z:
                        if z in errors:
                            continue
                        errors.append(z)
    return errors

def backpack_error_value(backPackErrors):
    errorScore=0
    for er in backPackErrors:
        errorScore += errorScoring[er]
    
    return errorScore

for index, line in enumerate(lines):
    if lineCount ==0:
        groupCount += 1
    lineCount += 1
    backpackItems = line.replace("\n","")
    groupList.append(backpackItems)
    
    if lineCount == 3:
        badge = find_the_badge(groupList)
        score = backpack_error_value(badge)
        totalErrorScore += score
        dicItem={"group": groupCount, "value": score}
        badgeGroups.append(dicItem)
        lineCount=0
        groupList=[]

print("Total error score is: " + str(totalErrorScore))
