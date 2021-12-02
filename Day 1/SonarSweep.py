
previousMeasurement = 0
largerCount = 0

f = open("input", "r")
for x in f:
    currentMeasuremnt = int(x)
    if (previousMeasurement != 0):
        if (currentMeasuremnt > previousMeasurement):
            largerCount += 1

    previousMeasurement = currentMeasuremnt  

print(largerCount)
