
horCount = 0
depCount = 0

f = open("input", "r")
for x in f:
    currentInput = x.split() 
    if currentInput[0] == "forward" :
        horCount += int(currentInput[1])
    else :
        if currentInput[0] == "up" :
            depCount -= int(currentInput[1])
        else :
            depCount += int(currentInput[1])

print(horCount * depCount)
