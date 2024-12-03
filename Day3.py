import re

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    list1 = []
    for line in lines:
        list1.append(line.strip())
    return list1

input = parseInput('input')

jj = 0
regexp = re.compile(r'[1234567890]')
solution = []
for jj in range(len(input)):
    ii = 0
    while ii < len(input[jj]):
        if input[jj][ii] == 'm' and input[jj][ii+1] == 'u' and input[jj][ii+2] == 'l' and input[jj][ii+3] == '(':
            ii = ii+4
            first = ''
            while True:
                if regexp.search(input[jj][ii]):
                    first += input[jj][ii]
                    ii += 1
                else: break
            if input[jj][ii] == ',': ii+=1
            else:
                ii+=1
                continue
            second = ''
            while True:
                if regexp.search(input[jj][ii]):
                    second += input[jj][ii]
                    ii += 1
                else: break
            if input[jj][ii] == ')':
                solution.append(int(first)*int(second))
        ii += 1

final = 0
for xx in range(len(solution)):
    final += solution[xx]

print("First Part "+ str(final))

jj = 0
solution2 = []
switch = True
for jj in range(len(input)):
    ii = 0
    while ii < len(input[jj]):
        if input[jj][ii] == 'd' and input[jj][ii+1] == 'o' and input[jj][ii+2] == '(' and input[jj][ii+3] == ')':
            switch = True
        if input[jj][ii] == 'd' and input[jj][ii+1] == 'o' and input[jj][ii+2] == 'n' and input[jj][ii+3] == '\'' and input[jj][ii+4] == 't' and input[jj][ii+5] == '(' and input[jj][ii+6] == ')':
            switch = False
        if switch and input[jj][ii] == 'm' and input[jj][ii+1] == 'u' and input[jj][ii+2] == 'l' and input[jj][ii+3] == '(':
            ii = ii+4
            first = ''
            while True:
                if regexp.search(input[jj][ii]):
                    first += input[jj][ii]
                    ii += 1
                else: break
            if input[jj][ii] == ',': ii+=1
            else:
                ii+=1
                continue
            second = ''
            while True:
                if regexp.search(input[jj][ii]):
                    second += input[jj][ii]
                    ii += 1
                else: break
            if input[jj][ii] == ')':
                solution2.append(int(first)*int(second))
        ii += 1

final2 = 0
for xx in range(len(solution2)):
    final2 += solution2[xx]

print("Second Part "+ str(final2))
