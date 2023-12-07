inputDoc = open("input.txt")

calDoc = inputDoc.read().split("\n")

calVal = []

# Part 1:
for i in range(len(calDoc)):
    tmp = []
    for j in range(len(calDoc[i])):
        if calDoc[i][j].isdigit():
            tmp.append(calDoc[i][j])
    calVal.append(int(tmp[0] + tmp[-1]))

print(sum(calVal))
