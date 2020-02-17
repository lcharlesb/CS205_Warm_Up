import csv, sqlite3, sys

def LoadData():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Drop tables if they exist
    c.execute("DROP TABLE IF EXISTS tblSales;")
    c.execute("DROP TABLE IF EXISTS tblRatings;")

    # Create tables for each csv file
    c.execute("CREATE TABLE tblSales (Rank, Name, Platform, Year, GlobalSales);")
    c.execute("CREATE TABLE tblRatings (Metascore, Name, Console, Userscore, ReleaseDate);")

    # Populate each table from respective csv file
    with open('sales.csv', 'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Rank'], i['Name'], i['Platform'], i['Year'], i['GlobalSales']) for i in dr]
    c.executemany("INSERT INTO tblSales (Rank, Name, Platform, Year, GlobalSales) VALUES (?, ?, ?, ?, ?);", to_db)

    with open('ratings.csv', 'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Metascore'], i['Name'], i['Console'], i['Userscore'], i['ReleaseDate']) for i in dr]
    c.executemany("INSERT INTO tblRatings (Metascore, Name, Console, Userscore, ReleaseDate) VALUES (?, ?, ?, ?, ?);", to_db)

    conn.commit()
    conn.close()

def CreateConnection(db):
    conn = None
    try:
        conn = sqlite3.connect(db)
    except Error as e:
        print(e)

    return conn

def ExecuteQuery(query, params):
    db = 'database.db'
    conn = CreateConnection(db)

    cur = conn.cursor()
    cur.execute(query, params)

    rows = cur.fetchall()
    for row in rows:
        print(row)

LoadData()

# TODO FRANK: Add your functions here(Delete this when added)

def searchSalesByTitle():
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
    # TODO LUKE: Add query here
    print(newArray)
    return newArray

def searchRatingsCritic(input):
    # needs query

def searchRatingsUser(input):
    # needs query

def searchRatingsTitle(input):
    # needs query

def ratingsError():
    print("Your ratings search does not contain a valid command.")

# TODO ISAAC: Add your functions here(Delete this when added)
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
    # TODO LUKE: Add query here
    print(newArray)


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
    # TODO LUKE: Add query here
    print(newArray)

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
        
def ratingMaster(input):
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

#============Validate Input Function==============#
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


# If program invoked directly
if __name__ == "__main__":

    userInput = ""

    while (userInput != "quit"):

        # Get user input
        userInput = input("")

        # Handle user input

    # Exit b/c user input == "quit"
    sys.exit()




