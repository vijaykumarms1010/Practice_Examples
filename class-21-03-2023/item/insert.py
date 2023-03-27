import sqlite3

def insertVaribleIntoTable(itemno,itemname,price,category):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO item
                          (itemno,itemname,price,category) 
                           VALUES 
                          (?,?,?,?)"""

        data_tuple = (itemno,itemname,price,category)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


insertVaribleIntoTable(3,'car',1200000,'drifting')