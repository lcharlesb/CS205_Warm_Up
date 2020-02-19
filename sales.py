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
    headers = list(('Rank', 'Name', 'Platform', 'Year', 'GlobalSales'))
    ExecuteQuery(query, params, headers)

def searchSalesTitle(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform, GlobalSales FROM tblSales"
        headers = list(('Name', 'Platform'))

    else:
        query = "SELECT GlobalSales, Platform FROM tblSales WHERE Name = ?"
        params.append(input)
        headers = list(('GlobalSales', 'Platform'))

    ExecuteQuery(query, params, headers)

def searchSalesYear(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform, Year FROM tblSales"
        headers = list(('Name', 'Platform', 'Year'))

    else:
        query = "SELECT Name, Platform, Year FROM tblSales WHERE Year = ?"
        params.append(input)
        headers = list(('Name', 'Platform', 'Year'))

    ExecuteQuery(query, params, headers)

def searchSalesPlatform(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Name, Platform FROM tblSales UNION SELECT Name, Console FROM tblRatings"
        headers = list(('Name', 'Platform'))

    else:
        query = "SELECT Name, Platform FROM tblSales WHERE Platform = ? UNION SELECT Name, Console FROM tblRatings WHERE Console = ?"
        params.append(input)
        params.append(input)
        headers = list(('Name', 'Platform'))

    ExecuteQuery(query, params, headers)

def searchSalesRank(input):
    query = ""
    params = list()
    headers = list()

    if(input.strip() == ""):
        query = "SELECT Rank, Name, Platform FROM tblSales"
        headers = list(('Rank', 'Name', 'Platform'))

    else:
        query = "SELECT Name FROM tblSales WHERE Rank = ?"
        params.append(input)
        headers = list(('Name'))

    ExecuteQuery(query, params, headers)

def salesError():
    print("Your sales search does not contain a valid command.")
