def splitInput(userInput):
    returnArray = list()

    splitArray = userInput.split(' ')

    returnArray.append(splitArray[0])
    splitArray.pop(0)

    if(len(splitArray) > 0):

        restOfString = ""

        for word in splitArray:
            restOfString += word + " "

        returnArray.append(restOfString.rstrip())

    else:

        returnArray.append(" ")

    return returnArray
