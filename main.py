from treeSorting import *

listOfWatnedClasses = []
UXFriendlyList = []
listOfNeededClasses = []

userBreak = False

masterListM = returnMasterList()

while not userBreak:
    print("Enter wanted class name or STOP to stop")
    userInput = input()
    if userInput == "STOP":
        userBreak = True
    else:
        try:
            z = masterListM[userInput]
            UXFriendlyList.append(userInput)
            listOfWatnedClasses.append(z)
            print("CLASS ADDED")
        except KeyError:
            print("INVALID CLASS")

print("Your final list is:")
print(UXFriendlyList)

def fullSearchWithPres(className):
    l = initSearch(className)
    return findHighestPres(turnTreeLeaves(l))

for i in UXFriendlyList:
    y = fullSearchWithPres(i)
    for b in y:
        if b in listOfNeededClasses:
            pass
        else:
            listOfNeededClasses.append(b)

print(listOfNeededClasses)

tenOrAbove = []
elevenOrAbove = []
twelveOrAbove = []

gradeReqs = {10: [], 11: [], 12: []}

for u in listOfWatnedClasses:
    b = u.returnAll()["gradeReq"]
    if b == 10:
        gradeReqs[10].append(b)
    elif b == 11:
        gradeReqs[11].append(b)
    elif b == 12:
        gradeReqs[12].append(b)
    
print(gradeReqs)
