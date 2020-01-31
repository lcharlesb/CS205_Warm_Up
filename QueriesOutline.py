# Help Command

# Load Command

# =============Sales=========== #

# searchGlobalSales
    # base:
    query = "SELECT Name, Platform, GlobalSales FROM tblSales"
    # by title:
    query = "SELECT GlobalSales FROM tblSales WHERE Name = ?"
# searchYear
    # base:
    query = "SELECT Name, Platform, Year FROM tblSales"
    # by year:
    query = "SELECT Name, Platform, Year FROM tblSales WHERE Year = ?"
# searchPlatform
    # base:
    query = "(SELECT Name, Platform FROM tblSales) UNION (SELECT Name, Console FROM tblRatings)"
    # by platform:
    query = "(SELECT Name, Platform FROM tblSales WHERE Platform = ?) UNION (SELECT Name, Console FROM tblRatings WHERE Console = ?)"
# searchRank
    # base:
    query = "SELECT Rank, Name, Platform FROM tblSales"
    # by rank:
    query = "SELECT Name FROM tblSales WHERE Rank = ?"

# ===========Ratings========== #

# searchTitle
    # base:
    query = "(SELECT Name, Platform FROM tblSales) UNION (SELECT Name, Console FROM tblRatings)"
    # by title:
    query = "SELECT Name FROM tblSales WHERE Name = ?"
# searchMetascore
    # base:
    query = "SELECT Metascore, Name FROM tblRatings"
    # by metascore:
    query = "SELECT Name, Metascore FROM tblRatings WHERE Metascore = ?"
# searchUserScore
    # base:
    query = "SELECT Userscore, Name FROM tblRatings"
    # by userscore:
    query = "SELECT Name, Userscore FROM tblRatings WHERE Userscore = ?"
