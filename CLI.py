import csv, sqlite3, sys

def LoadData():

    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    # Drop tables if they exist
    c.execute("DROP TABLE IF EXISTS tblSales;")
    c.execute("DROP TABLE IF EXISTS tblScores;")

    # Create tables for each csv file
    c.execute("CREATE TABLE tblSales (Rank, Name, Platform, Year, GlobalSales);")
    c.execute("CREATE TABLE tblScores (Metascore, Name, Console, Userscore, ReleaseDate);")

    # Populate each table from respective csv file
    with open('vgsales.csv', 'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Rank'], i['Name'], i['Platform'], i['Year'], i['GlobalSales']) for i in dr]
    c.executemany("INSERT INTO tblSales (Rank, Name, Platform, Year, GlobalSales) VALUES (?, ?, ?, ?, ?);", to_db)

    with open('result.csv', 'r') as fin:
        dr = csv.DictReader(fin)
        to_db = [(i['Metascore'], i['Name'], i['Console'], i['Userscore'], i['ReleaseDate']) for i in dr]
    c.executemany("INSERT INTO tblScores (Metascore, Name, Console, Userscore, ReleaseDate) VALUES (?, ?, ?, ?, ?);", to_db)

    conn.commit()
    conn.close()

LoadData()

# If program invoked directly
if __name__ == "__main__":

    userInput = ""

    while (userInput != "quit"):

        # Get user input
        userInput = input("")

        # Handle user input

    # Exit b/c user input == "quit"
    sys.exit()
