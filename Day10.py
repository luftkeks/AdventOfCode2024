def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    lists = []
    for line in lines:
        lists.append((list(map(int,line.strip()))))
    return lists

def findZeros(maps):
    zeros = []
    for yy in range(len(maps)):
        for xx in range(len(maps[yy])):
            if maps[yy][xx] == 0:
                zeros.append((yy,xx))
    return zeros

def findNext(maps, position, nextNumber) -> set:
    if maps[position[0]][position[1]] == 9:
        return {(position, 9)}
    result = {}
    if position[0] > 0 and maps[position[0]-1][position[1]] == nextNumber:
        result.update(findNext(maps, (position[0]-1, position[1]), nextNumber+1))
    if position[1] > 0 and maps[position[0]][ position[1]-1] == nextNumber:
        result.update(findNext(maps, (position[0], position[1]-1), nextNumber+1))
    if position[0] < len(maps)-1 and maps[position[0]+1][ position[1]] == nextNumber:
        result.update(findNext(maps, (position[0]+1, position[1]), nextNumber+1))
    if position[1] < len(maps[0])-1 and maps[position[0]][ position[1]+1] == nextNumber:
        result.update(findNext(maps, (position[0], position[1]+1), nextNumber+1))
    return result

def findNext2(maps, position, nextNumber) -> int:
    if maps[position[0]][position[1]] == 9:
        return 1
    result = 0
    if position[0] > 0 and maps[position[0]-1][position[1]] == nextNumber:
        result += findNext2(maps, (position[0]-1, position[1]), nextNumber+1)
    if position[1] > 0 and maps[position[0]][ position[1]-1] == nextNumber:
        result += findNext2(maps, (position[0], position[1]-1), nextNumber+1)
    if position[0] < len(maps)-1 and maps[position[0]+1][ position[1]] == nextNumber:
        result += findNext2(maps, (position[0]+1, position[1]), nextNumber+1)
    if position[1] < len(maps[0])-1 and maps[position[0]][ position[1]+1] == nextNumber:
        result += findNext2(maps, (position[0], position[1]+1), nextNumber+1)
    return result


maps = parseInput('input')
zeros = findZeros(maps)

total = 0
total2 = 0
for zero in zeros:
    nines = findNext(maps, zero, 1)
    total += len(nines)
    total2 += findNext2(maps, zero, 1)
print(total, total2)
