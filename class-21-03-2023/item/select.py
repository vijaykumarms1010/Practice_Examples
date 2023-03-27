import sqlite3

def getDeveloperInfo(itemno):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from item where itemno = ?"""
        cursor.execute(sql_select_query, (itemno,))
        records = cursor.fetchall()
        print("Printing ID ", itemno)
        for row in records:
            print("itemno  = ", row[0])
            print("itemname  = ", row[1])
            print("price  = ", row[2])
            print("category  = ", row[3])
            
            
        else:
            print("no empno found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(3)