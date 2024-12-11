def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    return map(int, lines[0].split(' '))

def blink(list1:list) -> list:
    newList = []
    for item in list1:
        if item == 0:
            newList.append(1)
        elif len(str(item))%2 ==0:
            asList = list(str(item))
            lenght = len(asList)
            firstPart = asList[0:lenght//2]
            secondPart = asList[lenght//2:]
            newList.append(int(''.join(firstPart)))
            newList.append(int(''.join(secondPart)))
        else:
            newList.append(item*2024)
    return newList

test = parseInput('input')
for ii in range(75):
    test = blink(test)
    print(ii)
print('End of First: ', len(test))
