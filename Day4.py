def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    list1 = []
    for line in lines:
        list1.append(line.strip())
    return list1

def joinHori(input: list, start: int,  other: int):
    return ''.join(input[other][start:start+4])

def joinVerti(input: list, start: int,  other: int):
    result = ''
    for ii in range(start, start+4):
        result += input[ii][other]
    return result

def joinDiaRight(input: list, xx: int,  yy: int):
    result = ''
    ii = 0
    while ii<4:
        result += input[yy+ii][xx+ii]
        ii += 1
    return result

def joinDiaLeft(input: list, xx: int,  yy: int):
    result = ''
    ii = 0
    while ii<4:
        result += input[yy+ii][xx-ii]
        ii += 1
    return result



input = parseInput('input')



count = 0
for yy in range(len(input)):
    for xx in range(len(input[yy])-3):
        value = joinHori(input, xx, yy)
        if value == 'XMAS' or value == 'SAMX':
            count +=1

for xx in range(len(input[yy])):
    for yy in range(len(input)-3):
        value = joinVerti(input, yy , xx)
        if value == 'XMAS' or value == 'SAMX':
            count +=1

for yy in range(len(input[yy])-3):
    for xx in range(len(input)-3):
        value = joinDiaRight(input, xx , yy)
        if value == 'XMAS' or value == 'SAMX':
            count +=1

for yy in range(len(input[yy])-3):
    for xx in range(3,len(input)):
        value = joinDiaLeft(input, xx , yy)
        if value == 'XMAS' or value == 'SAMX':
            count +=1

print("first value: " + str(count))


count2 = 0
def checkX1(input: list, xx: int,  yy: int):
    if input[yy][xx] == 'M' and input[yy][xx+2] == 'S' and input[yy+2][xx] == 'M' and input[yy+2][xx+2] == 'S' and input[yy+1][xx+1] == 'A':
        return 1
    else:
        return 0

def checkX2(input: list, xx: int,  yy: int):
    if input[yy][xx] == 'S' and input[yy][xx+2] == 'M' and input[yy+2][xx] == 'S' and input[yy+2][xx+2] == 'M' and input[yy+1][xx+1] == 'A':
        return 1
    else:
        return 0

def checkX3(input: list, xx: int,  yy: int):
    if input[yy][xx] == 'S' and input[yy][xx+2] == 'S' and input[yy+2][xx] == 'M' and input[yy+2][xx+2] == 'M' and input[yy+1][xx+1] == 'A':
        return 1
    else:
        return 0

def checkX4(input: list, xx: int,  yy: int):
    if input[yy][xx] == 'M' and input[yy][xx+2] == 'M' and input[yy+2][xx] == 'S' and input[yy+2][xx+2] == 'S' and input[yy+1][xx+1] == 'A':
        return 1
    else:
        return 0


for yy in range(len(input)-2):
    for xx in range(len(input[yy])-2):
        count2 += checkX1(input, xx, yy)
        count2 += checkX3(input, xx, yy)
        count2 += checkX2(input, xx, yy)
        count2 += checkX4(input, xx, yy)

print("second value: " + str(count2))
