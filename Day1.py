

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    list1 = []
    list2 = []
    for line in lines:
        line = line.split('   ')
        list1.append(int(line[0].strip()))
        list2.append(int(line[1].strip()))
    return list1, list2


list1, list2 = parseInput('inputDay1.txt')

list1.sort(), list2.sort()

totalSum: int = 0
similarity: int = 0
for ii in range(len(list1)):
    totalSum += abs(list1[ii] - list2[ii])
    sim = 0
    for jj in range(len(list2)):
        if list1[ii] == list2[jj]:
            sim += 1
    similarity += sim*list1[ii]
        

print("Answer part one: " + str(totalSum))
print("Answer part two: " + str(similarity))