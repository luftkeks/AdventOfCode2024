import copy

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    list1 = []
    for line in lines:
        line = line.split(' ')
        lili = []
        for ii in range(len(line)):
            lili.append(int(line[ii].strip()))
        list1.append(lili)
    return list1

lists = parseInput('inputDay2.txt')
#lists = parseInput('test.txt')

def checkList(list1: list):
    parity:int = list1[1] - list1[0]
    for ii in range(1,len(list1)):
        test:int = list1[ii] - list1[ii-1]
        if (test == 0 or abs(test) > 3 or test*parity < 0):
            return 0
    return 1

def checkList2(list1: list):
    if checkList(copy.deepcopy(list1)) == 1:
        return 1
    else:
        for ii in range(0,len(list1)):
            testList = copy.deepcopy(list1)
            del(testList[ii])
            if checkList(testList) == 1: return 1
    return 0

safeLists = 0
safeLists2 = 0
for ii in range(len(lists)):
    list1 = lists[ii]
    safeLists += checkList(copy.deepcopy(list1))
    safeLists2 += checkList2(copy.deepcopy(list1))

print("Answer part one: " + str(safeLists))
print("Answer part two: " + str(safeLists2))
