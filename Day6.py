import re

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    list1 = []
    line1 = 0
    position = 0
    for line in range(len(lines)):
        list1.append(list(lines[line].strip()))
        if lines[line].find('^') != -1:
            position = lines[line].find('^')
            line1 = line
    return list1, position, line1


lab, x, y = parseInput('inputDay6.txt')

def walk1(lab: list, x:int, y:int):
    lab[y][x] = 'X'
    inside = True
    direction = 'N'
    while inside:
        match direction:
            case 'N': y = y-1
            case 'S': y = y+1
            case 'W': x = x-1
            case 'O': x = x+1
        if x < 0 or y < 0 or y >= len(lab) or x >= len(lab[y]):
            inside = False
            return lab
        if lab[y][x] == '#':
            match direction:
                case 'N': 
                    direction = 'O'
                    y = y+1
                case 'S': 
                    direction = 'W'
                    y = y-1
                case 'W': 
                    direction = 'N'
                    x = x+1
                case 'O': 
                    direction = 'S'
                    x = x-1
        else:
            lab[y][x] = 'X'
            
def walk2(lab: list, x:int, y:int) -> bool:
    lab[y][x] = 'X'
    inside = True
    direction = 'N'
    while inside:
        match direction:
            case 'N': y = y-1
            case 'S': y = y+1
            case 'W': x = x-1
            case 'O': x = x+1
        if x < 0 or y < 0 or y >= len(lab) or x >= len(lab[y]):
            return False
        if lab[y][x] == direction:
            return True
        if lab[y][x] == '#' or lab[y][x] == 'Z':
            match direction:
                case 'N': 
                    direction = 'O'
                    y = y+1
                case 'S': 
                    direction = 'W'
                    y = y-1
                case 'W': 
                    direction = 'N'
                    x = x+1
                case 'O': 
                    direction = 'S'
                    x = x-1
        else:
            lab[y][x] = direction

def printLab(lab):
    print("New Lab")
    for line in lab:
        print(''.join(line))

lab1 = walk1(lab, x, y)

steps = 0
for row in lab1:
    for point in row:
        if point == 'X': steps +=1
print("Answer first: " + str(steps))

count = 0
for y1 in range(len(lab1)):
    for x1 in range(len(lab1[y1])):
        if lab1[y1][x1] == 'X':
            lab, x, y = parseInput('inputDay6.txt')
            lab[y1][x1] = 'Z'
            if walk2(lab, x, y):
                count +=1


print("Answer second: " + str(count))