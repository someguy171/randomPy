# create an empty dictionary to store the alphabet
letters = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

# for bases 2 to 9, numbers don't change
for num in range(0,10):
    letters[str(num)] = num

# for bases 10 to 26, each letter of the alphabet corresponds to numbers 10 to 35
for count, i in enumerate(alphabet):
    letters[i] = int(count)+10


def main():
    print("The following program supports bases 2 to 36.\n")
    # get the original number, its base, and the target base from the user
    originalStrNum, originalBase, targetBase = input("Enter a number: "), 0, 0

    # clean the input, so any letters are replaced with their corresponding value
    originalNum = cleanNum(originalStrNum)
    
    # ensure the number's base is between 2 and 26, and is an integer
    while originalBase < 2 or originalBase > 36 or not isinstance(originalBase, int):
        originalBase = int(input("What base was that number in? "))
    
    # check that the input can be in the base provided
    # see the checkMax function for more details
    if not checkMax(list(originalNum), originalBase):
        # if the input is invalid, stop the program
        print("Your number is not in base", str(originalBase) + ".\nPlease run the program again.")
        raise SystemExit(0)
    
    # ensure the target base is between 2 and 26, and is an integer
    while targetBase < 2 or targetBase > 36 or not isinstance(targetBase, int):
        targetBase = int(input("What base do you want to convert to? "))
    
    # convert the number to denary
    num = to10(originalNum, originalBase)
    
    # convert the new denary number to the target base
    toPass = []
    remList = getRems(num, targetBase, toPass)
    remList.reverse()
    remList = convertToBase(remList)
    
    # append each value in the converted list to a string, and output that string
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
