def searchRatings(input):
    inputArray = input.split()

    # separating rating command from rest of input
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

    # calls each individual function (criticRating/userRating/title)
    if(newArray[0] == "criticRating" or newArray[0] == "CriticRating"):
        searchRatingsCritic(newArray[1])
    elif(newArray[0] == "userRating" or newArray[0] == "UserRating"):
        searchRatingsUser(newArray[1])
    elif(newArray[0] == "title" or newArray[0] == "Title"):
        searchRatingsTitle(newArray[1])
    else:
        ratingsError()


def searchRatingsCritic(input):
    # needs query

def searchRatingsUser(input):
    # needs query

def searchRatingsTitle(input):
    # needs query

def ratingsError():
    print("Your rating does not contain a valid command.")
