import sqlite3

def getDeveloperInfo(taskid):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from task where taskid = ?"""
        cursor.execute(sql_select_query, (taskid,))
        records = cursor.fetchall()
        print("Printing TaskId ", taskid)
        for row in records:
            print("taskid  = ", row[0])
            print("taskname  = ", row[1])
            print("priority  = ", row[2])
            
            
            
        else:
            print("no Itemno found")
            
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

getDeveloperInfo(1)