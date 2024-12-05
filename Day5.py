
def parseInput(file: str):
    dataFile = open(file, mode = 'r', encoding = 'utf-8-sig')
    lines = dataFile.readlines()
    dataFile.close()
    pairs = []
    numbers = []
    for line in lines:
        if line.strip() == '':
            continue
        elif '|' in line:
            pairs.append(list(map(int,(line.strip().split('|')))))
        else: 
            numbers.append(list(map(int,(line.strip()).split(','))))
    return pairs, numbers


def check(nums:list, pairs:list):
    ii=0
    while ii < len(nums):
        for pair in pairs:
            if pair[0] == nums[ii]:
                jj = ii
                while jj >= 0:
                    if pair[1] == nums[jj]:
                        return 0
                    jj -=1
        ii +=1
    return nums[int(len(nums)/2)]

def check2(nums:list, pairs:list):
    ii=0
    while ii < len(nums):
        for pair in pairs:
            if pair[0] == nums[ii]:
                jj = ii
                while jj >= 0:
                    if pair[1] == nums[jj]:
                        nums[jj] = pair[0]
                        nums[ii] = pair[1]
                        return check2(nums, pairs)
                    jj -=1
        ii +=1
    return nums[int(len(nums)/2)]


pairs, numbers = parseInput('input')

middle = 0
wrongNums =[]
for nums in numbers:
    answer = check(nums, pairs)
    middle += answer
    if answer == 0:
        wrongNums.append(nums)

print("answer first: " + str(middle))

middle2 = 0
for nums in wrongNums:
    answer = check2(nums, pairs)
    middle2 += answer

print("answer first: " + str(middle2))
