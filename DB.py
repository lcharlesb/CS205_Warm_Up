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
    if(len(rows) == 0):
        print("'" + str(params[0]) + "' not present in database - please check input and try again.")
    else:
        for row in rows:
            print(row)
