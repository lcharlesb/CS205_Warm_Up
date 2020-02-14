#Isaac A-P
from CLI import *

def salesMaster(identifyFirst):

    inputArray = identifyFirst.split()

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


    if(identifyFirst == "Platform" or identifyFirst == "platform"):
        searchSalesPlatform(identifyQuery)
    if(identifyFirst == "Rank" or identifyFirst == "rank"):
        searchSalesRank(identifyQuery)
    if(identifyFirst == "Year" or identifyFirst == "year"):
        seachSalesYear(identifyQuery)
    if(identifyFirst == "Title" or identifyFirst == "title"):
        searchGlobalSales(identifyQuery)


def searchSalesPlatform(newArray):
    # Query
    # Print
    inputArray = newArray.split()

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
    # TODO ADD A QUERY CALL HERE
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


    if(newArray[0] == "sales" or newArray[0] == "Sales"):
         salesMaster(newArray[1])

    if(newArray[0] == "ratings" or newArray[0] == "Ratings"):
        ratingMaster(newArray[1])

    else:
        print("Invalid Input")




    




def searchSalesRank(newArray):
    # Query
    # Print
    inputArray = newArray.split()

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
    # TODO ADD A QUERY CALL HERE
    print(newArray)
