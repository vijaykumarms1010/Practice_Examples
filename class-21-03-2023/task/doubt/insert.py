import sqlite3

def insertVaribleIntoTable(taskid,taskname,priority):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO task
                          (taskid,taskname,priority) 
                           VALUES 
                          (?,?,?)"""

        data_tuple = (taskid,taskname,priority)
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


insertVaribleIntoTable(1,'Create db',1)