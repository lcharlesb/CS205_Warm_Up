from splitInput import splitInput
from DB import ExecuteQuery

#======Rating Master======#
def ratingsMaster(input):

    if(input.strip() == ""):

        baseRatings()

    else:

        splitArray = splitInput(str(input))

        # calls each individual function (criticRating/userRating/title)
        if(splitArray[0].lower() == "criticrating"):
            searchRatingsCritic(splitArray[1])
        elif(splitArray[0].lower() == "userrating"):
            searchRatingsUser(splitArray[1])
        elif(splitArray[0].lower() == "title"):
            searchRatingsTitle(splitArray[1])
        else:
            ratingsError()

#=======Ratings=======#
def baseRatings():
    query = "SELECT * FROM tblRatings"
    params = list()
    ExecuteQuery(query, params)

def searchRatingsCritic(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Metascore, Name FROM tblRatings"

    else:
        query = "SELECT Name, Metascore FROM tblRatings WHERE Metascore = ?"
        params.append(input)

    ExecuteQuery(query, params)

def searchRatingsUser(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Userscore, Name FROM tblRatings"

    else:
        query = "SELECT Name, Userscore FROM tblRatings WHERE Userscore = ?"
        params.append(input)

    ExecuteQuery(query, params)

def searchRatingsTitle(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform FROM tblSales UNION SELECT Name, Console FROM tblRatings"

    else:
        query = "SELECT Name FROM tblSales WHERE Name = ?"
        params.append(input)

    ExecuteQuery(query, params)

def ratingsError():
    print("Your ratings search does not contain a valid command.")
