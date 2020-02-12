#Isaac A-P

def salesMaster(identifyFirst):

    inputArray = identifyFirst

    if (len(inputArray) > 2):

        i = len(inputArray) - 1
        print(inputArray[i])
        newArray = [0, 0]
        newArray[0] = inputArray[0]
        s = ""
        while (i > 0):
            print(i)
            s = s + inputArray[-i]
            s = s + " "
            i -= 1

    newArray[1] = s
    identifyFirst = newArray[0]
    identifyQuery = newArray[1]
    identifyFirst.lower()


    if(identifyFirst == "platform"):
        searchSalesPlatform(identifyQuery)
    if (identifyFirst == "rank"):
        searchSalesRank(identifyQuery)
    if(identifyFirst == "year"):
        seachSalesYear(identifyQuery)
    if(identifyFirst == "global"):
        searchGlobalSales(identifyQuery)

def ratingMaster(newArray):


def searchSalesPlatform(newArray):
    # Query
    # Print
    inputArray = userInput.split()

    if (len(inputArray) > 2):

        i = len(inputArray) - 1
        print(inputArray[i])
        newArray = [0, 0]
        newArray[0] = inputArray[0]
        s = ""
        while (i > 0):
            print(i)
            s = s + inputArray[-i]
            s = s + " "
            i -= 1

    newArray[1] = s
    print(newArray)

def validateInput():

    inputArray = userInput.split()

    if (len(inputArray) > 2):

        i = len(inputArray) - 1
        print(inputArray[i])
        newArray = [0, 0]
        newArray[0] = inputArray[0]
        s = ""
        while (i > 0):
            print(i)
            s = s + inputArray[-i]
            s = s + " "
            i -= 1

    newArray[1] = s
    print(newArray)

    if(newArray[0] == "sales"):
        salesMaster(newArray[1])

    if(newArray[0] == "ratings"):
        ratingMaster(newArray[1])



    




def searchSalesRank():
    # Query
    # Print
