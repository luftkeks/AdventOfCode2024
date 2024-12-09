import copy

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    return list(lines[0].strip())

def extract(string: list) -> list:
    extract = []
    for elem in range(len(string)):
        ii = 0
        for ii in range(int(string[elem])):
            if elem%2 == 0:
                extract.append(elem//2)
            else:
                extract.append('.')
            ii +=1
    return extract

def compact(string: list)-> list:
    last = len(string) - 1
    for ii in range(len(string)):
        if ii >= last: break
        if string[ii] == '.':
            for jj in range(last, 0,-1):
                if string[jj] != '.':
                    last = jj
                    string[ii] = string[jj]
                    string[jj] = '.'
                    break
#        print(''.join(map(str,string)))
    return string

def calcChecksum(string: list) -> int:
    result = 0
    for ii in range(len(string)):
        if string[ii] != '.': result += ii*int(string[ii])
    return result

def compact2(string: list) -> list:
    fileSize = 0
    lastID = string[-1]
    length = len(string)
    lastOne = 0
    moved = []
    for ii in range(length-1, -1 ,-1):
        if ii <= lastOne: break
        if string[ii] != '.' and lastID == string[ii]:              # count
            fileSize += 1
        elif lastID == '.' and  lastID != string[ii]:
            lastID = string[ii]
            fileSize = 1
        elif lastID != '.' and lastID != string[ii]:
            spacecount = 0
            if not lastID in moved:
                for jj in range(lastOne, ii+1):                       # find space
                    if string[jj] == '.': spacecount += 1
                    else: spacecount = 0
                    if spacecount >= fileSize:
                        if fileSize == 1: lastOne = jj
                        difference = ii-jj+fileSize
                        for kk in range(jj-fileSize+1, jj+1):       # move
                            string[kk] = string[difference + kk]
                            string[difference + kk] = '.'
                        break
                moved.append(lastID)
#                print(''.join(map(str,string)))
            fileSize = 1                                            # prepare next
            lastID = string[ii]
            spacecount = 0
    return string

string = parseInput('inputDay9.txt')
extracted = extract(string)
sorted1 = compact(copy.deepcopy(extracted))
print('Result day 8 first:', calcChecksum(sorted1))

sorted2 = compact2(copy.deepcopy(extracted))
print('Result day 8 second:', calcChecksum(sorted2))