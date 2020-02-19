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
    headers = list(('CriticScore', 'Name', 'Console', 'UserScore', 'ReleaseDate'))
    ExecuteQuery(query, params, headers)

def searchRatingsCritic(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Metascore, Name FROM tblRatings"
        headers = list(('CriticScore', 'Name'))

    else:
        query = "SELECT Name, Metascore FROM tblRatings WHERE Metascore = ?"
        params.append(input)
        headers = list(('Name', 'CriticScore'))

    ExecuteQuery(query, params, headers)

def searchRatingsUser(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Userscore, Name FROM tblRatings"
        headers = list(('UserScore', 'Name'))

    else:
        query = "SELECT Name, Userscore FROM tblRatings WHERE Userscore = ?"
        params.append(input)
        headers = list(('Name', 'UserScore'))

    ExecuteQuery(query, params, headers)

def searchRatingsTitle(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform FROM tblSales UNION SELECT Name, Console FROM tblRatings"
        headers = list(('Name', 'Platform'))

    else:
        query = "SELECT Name FROM tblSales WHERE Name = ?"
        params.append(input)
        headers = list(('Name'))

    ExecuteQuery(query, params, headers)

def ratingsError():
    print("Your ratings search does not contain a valid command.")
