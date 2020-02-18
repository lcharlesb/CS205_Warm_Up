from splitInput import splitInput
from DB import ExecuteQuery

#======Sales Master======#
def salesMaster(input):

    if(input.strip() == ""):

        baseSales()

    else:

        splitArray = splitInput(str(input))

        if(splitArray[0].lower() == "platform"):
            searchSalesPlatform(splitArray[1])
        elif(splitArray[0].lower() == "rank"):
            searchSalesRank(splitArray[1])
        elif(splitArray[0].lower() == "year"):
            searchSalesYear(splitArray[1])
        elif(splitArray[0].lower() == "title"):
            searchSalesTitle(splitArray[1])
        else:
            salesError()

#========Sales========#
def baseSales():
    query = "SELECT * FROM tblSales"
    params = list()
    ExecuteQuery(query, params)

def searchSalesTitle(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform, GlobalSales FROM tblSales"

    else:
        query = "SELECT GlobalSales, Platform FROM tblSales WHERE Name = ?"
        params.append(input)

    ExecuteQuery(query, params)

def searchSalesYear(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform, Year FROM tblSales"

    else:
        query = "SELECT Name, Platform, Year FROM tblSales WHERE Year = ?"
        params.append(input)

    ExecuteQuery(query, params)

def searchSalesPlatform(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform FROM tblSales UNION SELECT Name, Console FROM tblRatings"

    else:
        query = "SELECT Name, Platform FROM tblSales WHERE Platform = ? UNION SELECT Name, Console FROM tblRatings WHERE Console = ?"
        params.append(input)
        params.append(input)

    ExecuteQuery(query, params)

def searchSalesRank(input):
    query = ""
    params = list()

    if(input.strip() == ""):
        query = "SELECT Rank, Name, Platform FROM tblSales"

    else:
        query = "SELECT Name FROM tblSales WHERE Rank = ?"
        params.append(input)

    ExecuteQuery(query, params)

def salesError():
    print("Your sales search does not contain a valid command.")
