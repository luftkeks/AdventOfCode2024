import copy

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    liste = []
    maxValue = (len(lines[0].strip()), len(lines), 'max')
    for yy in range(len(lines)):
        line = list(lines[yy].strip())
        for xx in range(len(line)):
            if line[xx] != '.':
                liste.append((xx, yy, line[xx]))
    return maxValue, liste, lines

def genAntiNode1(tupel1, tupel2):
    xxDis = abs(tupel1[0]-tupel2[0])
    yyDis = abs(tupel1[1]-tupel2[1])
    if (tupel1[0] > tupel2[0] and tupel1[1] > tupel2[1]) or (tupel1[0] < tupel2[0] and tupel1[1] < tupel2[1]):
        antiTupel1 = (min(tupel1[0],tupel2[0]) - xxDis, min(tupel1[1],tupel2[1]) - yyDis, '#')
        antiTupel2 = (max(tupel1[0],tupel2[0]) + xxDis, max(tupel1[1],tupel2[1]) + yyDis, '#')
    else:
        antiTupel1 = (max(tupel1[0],tupel2[0]) + xxDis, min(tupel1[1],tupel2[1]) - yyDis, '#')
        antiTupel2 = (min(tupel1[0],tupel2[0]) - xxDis, max(tupel1[1],tupel2[1]) + yyDis, '#')
    return antiTupel1, antiTupel2

def genAntiNode2(tupel1, tupel2, maximum):
    xxDis = abs(tupel1[0]-tupel2[0])
    yyDis = abs(tupel1[1]-tupel2[1])
    result = []
    for ii in range(50):
        if (tupel1[0] > tupel2[0] and tupel1[1] > tupel2[1]) or (tupel1[0] < tupel2[0] and tupel1[1] < tupel2[1]):
            antiTupel1 = (min(tupel1[0],tupel2[0]) - xxDis*ii, min(tupel1[1],tupel2[1]) - yyDis*ii, '#')
            antiTupel2 = (max(tupel1[0],tupel2[0]) + xxDis*ii, max(tupel1[1],tupel2[1]) + yyDis*ii, '#')
        else:
            antiTupel1 = (max(tupel1[0],tupel2[0]) + xxDis*ii, min(tupel1[1],tupel2[1]) - yyDis*ii, '#')
            antiTupel2 = (min(tupel1[0],tupel2[0]) - xxDis*ii, max(tupel1[1],tupel2[1]) + yyDis*ii, '#')
        if testAntiTupel(antiTupel1, maximum): result.append(antiTupel1)
        if testAntiTupel(antiTupel2, maximum): result.append(antiTupel2)
    return result

def testAntiTupel(tupel, max) -> bool:
    return tupel[0] >= 0 and tupel[1] >=0 and tupel[0] >= 0 and tupel[0] < maxValue[0] and tupel[1] < maxValue[1]

maxValue, liste, lines = parseInput('inputDay8.txt')

hashmap = {}
for value in liste:
    hashmap[value[2]] = []

for value in liste:
    hashmap.get(value[2], []).append(value)

solution = {}
solution2 = {}
for key, liste in hashmap.items():
    for value1 in range(len(liste)):
        for value2 in range(value1+1, len(liste)):
            antiTupel1, antiTupel2 = genAntiNode1(liste[value1], liste[value2])
            if testAntiTupel(antiTupel1, maxValue): solution[antiTupel1] = 0
            if testAntiTupel(antiTupel2, maxValue): solution[antiTupel2] = 0
            anti = genAntiNode2(liste[value1], liste[value2], maxValue)
            for an in anti:
                if testAntiTupel(an, maxValue): solution2[an] = 0

counter1 = 0
for key in solution.keys():
    counter1 += 1

counter2 = 0
for key in solution2.keys():
    temp = list(lines[key[1]])
    temp[key[0]] = key[2]
    lines[key[1]] = ''.join(temp)
    counter2 += 1

print("solution1: ", counter1, "Solution 2:", counter2)

for line in lines:
    print(line,end="")