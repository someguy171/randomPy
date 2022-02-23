from doctest import OutputChecker


letters = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

for num in range(0,10):
    letters[str(num)] = num

for count, i in enumerate(alphabet):
    letters[i] = int(count)+10

print(letters)

def main():
    print("The following program supports bases 2 to 36.\n")
    # get the original number, its base, and the target base from the user
    originalBase, targetBase = 0, 0
    
    originalNum = input("Enter a number: ")
    
    while originalBase < 2 or originalBase > 36 or not isinstance(originalBase, int):
        originalBase = int(input("What base was that number in? "))
    
    while targetBase < 2 or targetBase > 36 or not isinstance(targetBase, int):
        targetBase = int(input("What base do you want to convert to? "))
    
    # if the original number is not denary, convert it to denary
    if originalBase != 10:
        num = to10(cleanNum(originalNum), originalBase)
        print("num", num)
    else:
        num = originalNum
        
    # convert the denary number to the target base
    toPass = []
    remList = getRems(num, targetBase, toPass)
    remList.reverse()
    
    final = ""
    for item in remList:
        final += str(item)
    
    print(originalNum, "in base", str(originalBase), "is", final + ".")


def checkMax(numString, base):
    maxVal = base - 1
    for char in numString:
        if letters[char] + 1 > base:
            
        # you need to find the max value of each base
        # this is fine for base 2-10, but then they start using letters
        # get the key from the key-pair value in the dict and use that to find the maxVal
        # or do something else idk
        
        
        # base 2 = 1
        # base 3 = 2
        # base 4 = 3
        # base 5 = 4
        # base 6 = 5
        # base 7 = 6
        # base 11 = a
        # base 12 = b


def cleanNum(numString):
    if numString.isnumeric():
        numList = [int(num) for num in numString]
    else:
        numList = list(numString)
        for char in numList:
            if not char.isnumeric():
                numList.append(letters[char.lower()])
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