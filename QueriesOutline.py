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
# searchPlatform
    # base:
    query = "(SELECT Name, Platform FROM tblSales) UNION (SELECT Name, Console FROM tblScores)"
    # by platform:
    query = "(SELECT Name, Platform FROM tblSales WHERE Platform = ?) UNION (SELECT Name, Console FROM tblScores WHERE Console = ?)"
# searchRank
    # base:
    query = "SELECT Rank, Name, Platform FROM tblSales"
    # by number:
    query = "SELECT Name FROM tblSales WHERE Rank = ?"

# ===========Ratings========== #

# searchTitle
    # base:
    query = "(SELECT Name, Platform FROM tblSales) UNION (SELECT Name, Console FROM tblScores)"
# searchMetacritic
    # base:
    query = "SELECT Metascore, Name FROM tblScores"
# searchUserScore
    # base:
    query = "SELECT Userscore, Name FROM tblScores"
