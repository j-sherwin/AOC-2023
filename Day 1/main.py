inputDoc = open("input.txt")

calDoc = inputDoc.read().split("\n")

numsDict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

numsArray = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]

calVal = []

# Part 2:
for i in range(len(calDoc)):
    tmp =[]

    for j in range(len(calDoc[i])):
        for k in range(len(numsArray)):
            if calDoc[i].startswith(numsArray[k], j):
                tmp.append(numsArray[k])

    if tmp[0] in numsDict:
        tmp[0] = numsDict[tmp[0]]

    if tmp[-1] in numsDict:
        tmp[-1] = numsDict[tmp[-1]]

    calVal.append(int(tmp[0] + tmp[-1]))

print(sum(calVal))
