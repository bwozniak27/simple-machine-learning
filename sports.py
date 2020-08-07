

def organizeList(listOfLines):
    word = ""
    listOfWords = []
    for line in listOfLines:
        temp = []
        for i, c in enumerate(line):
            if c == ',' or i == len(line) - 1:
                temp.append(word)
                word = ""
            else:
                word += c
        listOfWords.append(temp)
    return listOfWords

def makeLabels(listOfWords):
    dictLabels = {}
    for i, line in enumerate(listOfWords):
        if i == 0:
            pass
        else:
            if line[-1] in dictLabels:
                pass
            else:
                dictLabels[line[-1]] = {}
    for x in listOfWords[0]:
        for key in dictLabels:
            if x == listOfWords[0][-1]:
                pass
            else:
                dictLabels[key][x] = []
    return dictLabels



def trainModel(traineDict, listOfWords):
    for x, line in enumerate(listOfWords):
        if x == 0:
            pass
        else:
            species = line[-1]
            for i, word in enumerate(listOfWords[0]):
                if word == listOfWords[0][-1]:
                    pass
                else:
                    traineDict[species][word].append(float(line[i]))
    return traineDict

def CalculateAverages(trainedDict):
    AverageDict = {}
    for label in trainedDict:
        AverageDict[label] = {}
        for description in trainedDict[label]:
            AverageDict[label][description] = 0
            sum = 0.0
            for values in trainedDict[label][description]:
                sum += values
            sum = sum / len(trainedDict[label][description])
            AverageDict[label][description] = sum
    return AverageDict


def makePrediction(newStuff, AverageDict):
    print("calculating prediction...")
    difference = {}
    for label in AverageDict:
        difference[label] = {}
       # print("testing: ")
        for i, description in enumerate(AverageDict[label]):
            num = AverageDict[label][description]
           # print(num)
            difference[label][description] = pow((num - float(newStuff[i])), 2)
    print()
    print("difference: ")
    print(difference)

    accuracy = {}
    for label in difference:
        sum = 0.0
        for description in difference[label]:
            sum += difference[label][description]
        accuracy[label] = sum
    print()
  #  print("sum = ")
  #  print(sum)
    print()
    print(accuracy)
    minimum = 0
    minLabel = ""
    for i, labels in enumerate(accuracy):
        if i == 0:
            minimum = accuracy[labels]
            minLabel = labels
        elif accuracy[labels] < minimum:
            minimum = accuracy[labels]
            minLabel = labels
    return minLabel


def main():
    stuff = open("IRIS.csv", "r")
    listOfLines = []
    for x in range(148):
        listOfLines.append(stuff.readline())

    print(listOfLines)
    listOfWords = organizeList(listOfLines)
    print("and now for the new list: ")
    print(listOfWords)
    dictLabels = makeLabels(listOfWords)
    print("labels only: ")
    print(dictLabels)
    trainedModel = trainModel(dictLabels, listOfWords)
    print("fully trained: ")
    print(trainedModel)
    averages = CalculateAverages(trainedModel)
    print("now for the averages")
    print(averages)
    print("time for predictions")
    newStuff = organizeList(stuff.readlines())
    print(newStuff)
    print()
    for i, x in enumerate(newStuff):
      #  print("checking averages: ")
      #  print(averages)
        prediction = makePrediction(newStuff[i], averages)
        print("prediction: " + prediction + ", actual: " + newStuff[i][-1])

    stuff.close()

main()