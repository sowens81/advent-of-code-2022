import string

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

def check_backpack_errors(pocketOne, pocketTwo):
    listX = []
    listY = []
    errors = []
    
    for l in pocketOne:
        listX.append(l)
    
    for l in pocketTwo:
        listY.append(l)
    
    for i in listX :
        for l in listY:
            if i == l:
                if i in errors:
                    continue
                errors.append(i)
    return errors

def backpack_error_value(backPackErrors):
    errorScore=0
    for er in backPackErrors:
        errorScore += errorScoring[er]
    
    return errorScore

file = open("data.txt")
lines = file.readlines()

for index, line in enumerate(lines):

    backpackItems = line.replace("\n","")

    itemsPerPocket = len(backpackItems) / 2

    pocketOneItems= backpackItems[:itemsPerPocket]
    pocketTwoItems= backpackItems[-itemsPerPocket:]
    
    backPackErrorList= check_backpack_errors(pocketOneItems, pocketTwoItems)
    backPackErrorValue= backpack_error_value(backPackErrorList)
    totalErrorScore += backPackErrorValue
    print(backPackErrorList)
    print(backPackErrorValue)
    
print("The total backpack error score is: " + str(totalErrorScore))
