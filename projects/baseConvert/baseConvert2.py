letters = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

for num in range(0,10):
    letters[str(num)] = num

for count, i in enumerate(alphabet):
    letters[i] = int(count)+10


def main():
    print("The following program supports bases 2 to 36.\n")
    # get the original number, its base, and the target base from the user
    originalBase, targetBase = 0, 0
    
    originalStrNum = input("Enter a number: ")
    originalNum = cleanNum(originalStrNum)
    
    while originalBase < 2 or originalBase > 36 or not isinstance(originalBase, int):
        originalBase = int(input("What base was that number in? "))
    
    if not checkMax(list(originalNum), originalBase):
        print("Your number is not in base", str(originalBase) + ".\nPlease run the program again.")
        raise SystemExit(0)
    
    while targetBase < 2 or targetBase > 36 or not isinstance(targetBase, int):
        targetBase = int(input("What base do you want to convert to? "))
    
    # if the original number is not denary, convert it to denary
    if originalBase != 10:
        num = to10(originalNum, originalBase)
    else:
        num = originalNum
    
    # convert the denary number to the target base
    toPass = []
    remList = getRems(num, targetBase, toPass)
    remList.reverse()
    
    remList = convertToBase(remList)
    
    final = ""
    for item in remList:
        final += str(item)
    
    print(originalStrNum, "in base", str(targetBase), "is", final + ".")


def convertToBase(remList):
    outputList = []
    for item in remList:
        if item > 9:
            outputList.append(list(letters.keys())[list(letters.values()).index(item)])
        else:
            outputList.append(item)
    return outputList


def checkMax(numList, base):
    valueList = [value for value in letters.values()]
    for num in numList:
        if int(valueList[int(num)]) >= base:
            return False
    return True


def cleanNum(numString):
    if numString.isnumeric():
        numList = [int(num) for num in numString]
    else:
        numList = []
        for char in list(numString):
            if not char.isnumeric():
                numList.append(letters[char.lower()])
            else:
                numList.append(int(char))
    return numList


def to10(numList, originalBase):
    numList.reverse()
    output = [(num*originalBase**count) for count, num in enumerate(numList)]
    return sum(output)


def getRems(num, targetBase, remList):
    # if the number passed in is 0 (because the number cannot be divided by the target base anymore)
    if num != 0:
        # find the result of the number divided by the target base
        result = num // targetBase
        
        # append the remainder of this operation to a list
        remList.append(int(num) % targetBase)
        
        # repeat the process, using the result of the operation
        remList = getRems(result, targetBase, remList)
    
    # return a list of remainders from all the operations
    return remList
    

main()