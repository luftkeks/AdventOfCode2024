import copy

def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    list1 = []
    for line in lines:
        list1.append(line.strip())
    return list1

def testColumn(line: str) -> int:
    line = line.split(':')
    answer = int(line[0])
    question = []
    for num in line[1].strip().split(' '):
        question.append(int(num.strip()))
    if testLine(answer, question) == 0:
        return int(line[0])
    else: return 0

def testLine(answer: int, question: list) -> int:
    if len(question) == 1:
        return answer - question[0]
    else:
        last = question.pop()
        answer1 = 1
        if answer%last == 0:
            answer1 = testLine(answer//last, copy.deepcopy(question))
        answer2 = testLine(answer-last, copy.deepcopy(question))
        return answer1*answer2

result = 0
for line in parseInput('inputDay7.txt'):
    answer = testColumn(line)
    result += answer

print("answer first: ", str(result))

#3356953340963
#3356642658026

def testColumn2(line: str) -> int:
    line = line.split(':')
    answer = int(line[0])
    question = []
    for num in line[1].strip().split(' '):
        question.append(int(num.strip()))
    if testLine2(answer, question) == 0:
        return int(line[0])
    else: return 0

def testLine2(answer: int, question: list) -> int:
    if len(question) == 1:
        return answer - question[0]
    else:
        first = question[0]
        del(question[0])
        input1 = copy.deepcopy(question)
        input1[0] = input1[0] + first
        answer1 = testLine2(answer, input1)
        input2 = copy.deepcopy(question)
        input2[0] = input2[0] * first
        answer2 = testLine2(answer, input2)
        input3 = copy.deepcopy(question)
        input3[0] = int(str(first) + str(input3[0]))
        answer3 = testLine2(answer, input3)
        return answer1*answer2*answer3


result2 = 0
counter = 0
for line in parseInput('inputDay7.txt'):
    counter += 1
    answer = testColumn2(line)
    result2 += answer
    print("line: " + str(counter))

print("answer second: ", str(result2))
