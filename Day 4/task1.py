

file = open("data.txt")
lines = file.readlines()

errorLines=0

def validate_work(workingList):
    a = workingList[0]["first"]
    b = workingList[0]["last"]
    x = workingList[1]["first"]
    y = workingList[1]["last"]
    
    if a < x:
        if b > y:
            return True  
            
        
    if x < a:
        if y > b:
            return True
    
    if a == x:
        if b ==  y:
            return True
    
    return False
            

for index, line in enumerate(lines):
    workingList = []
    pairs = line.replace("\n","").split(",")
    
    for p in pairs:
        values = p.split("-")
        value = {"first": values[0],"last": values[1]}
        workingList.append(value)
        
    retval = validate_work(workingList)
    if retval == True:
        errorLines += 1
            
print( "There are " + str(errorLines) + " overlapping jobs.")