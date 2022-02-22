letters = {
    "a": 10,
    "b": 11,
    "c": 12,
    "d": 13,
    "e": 14,
    "f": 15
}

def digitCalc(char, base, i):
    return char * base**i


def conTo10(valString, startingBase):
    sum = 0
    index = 0
    for i in valString:
        if not i.isnumeric():
            valString[index] = letters[valString[index]]
        sum += digitCalc(int(valString[index]), int(startingBase), int(i))
        index += 1
    return sum


def div(num, remList, goalBase):
    val = int(num) // goalBase
    remList.append(int(num) % goalBase)
    if num != 0:
        div(val, remList, goalBase)
    return remList


startingBase = int(input("enter starting base: "))
goalBase = int(input("enter goal base: "))
val = input("enter value: ")

digits = [char for char in val]

if startingBase != 10:
    val = conTo10(str(val), startingBase)
    startingBase = 10

if startingBase == 10:
    remList = div(val, [], goalBase)
    remList.pop()
    remList.reverse()
    print(remList)
