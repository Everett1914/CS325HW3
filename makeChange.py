#Everett Williams
#14JUL17 as of 150755JUL17
#HW3 Problem 4
#Make Change program

def buildCoinsArr(coinsUsed, coinSet):
    start = len(coinsUsed)-1
    numCoinsUsed = []

    #initialize numCoinsUsed to 0.  This array will be used to track
    #the number of each coin that was used.
    for i in range(0, len(coinSet)):
            numCoinsUsed.append(0)

    #accumulate the coins
    while start != 0:
        numCoinsUsed[coinsUsed[start]] = numCoinsUsed[coinsUsed[start]]+1
        start = start - coinSet[coinsUsed[start]]
    return numCoinsUsed

#read data from amount.txt and store the coin denominations as integers into the
#list dataArray return unsorted array
def readWriteArray():
    with open('amount.txt') as data:
        lineCount = 0
        val = -1
        for line in data:
            if lineCount%2 == 0:
                dataArray = []
                line = line.split() # to deal with blank
                if line:            # lines (ie skip them)
                    for value in line:
                        num = int(value)
                        dataArray.append(num)
            elif lineCount%2 == 1:
                val = line.rstrip("\n")
                coinNum, coinsUsed = makeChange(dataArray, int(val))
                outPutToFile(dataArray, val, coinsUsed, coinNum)
            lineCount+=1

#write change results to change.txt
def outPutToFile(coinDenom, val, coinsUsed, coinNum):
    with open('change.txt', 'a') as outPutFile:
        for i in coinDenom:
            num = str(i)
            outPutFile.write(num + " ")
        outPutFile.write("\n")
        outPutFile.write(val)
        outPutFile.write("\n")
        for i in coinsUsed:
            num = str(i)
            outPutFile.write(num + " ")
        outPutFile.write("\n")
        outPutFile.write(str(coinNum))
        outPutFile.write("\n")


def makeChange(coinSet, value):
    numCoins=[]
    coinsUsed=[]

    #initialize the counting array (numCoins) with values infinity, since we know
    #no number is greater than infinity.  This ensures that a count is made upon
    #a initial visit
    for i in range(0, value + 1):
        if i == 0:
            numCoins.append(0)
        else:
            numCoins.append(float('inf'))

    #initialize the tracking array (coinsUsed) to track the coin with the greatest
    #value that was used to make the particular value represented with the array
    #indice.  The array was initialized with inf since that value will never be
    #a valid denomination.
    for i in range(0, value + 1):
            coinsUsed.append(float('inf'))

    for j in range(len(coinSet)):
        for i in range(1, value + 1):
            if numCoins[i] > (1 + numCoins[i - coinSet[j]]):
                numCoins[i] = (1 + numCoins[i - coinSet[j]])
                coinsUsed[i] = j

    coins=buildCoinsArr(coinsUsed,coinSet)
    return numCoins[-1], coins

readWriteArray()
