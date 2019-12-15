import sqlite3 as lite

# Database CRUD operations


class DatabaseOperations(object):

    def __init__(self):
        global dbconn
        try:
            dbconn = lite.connect('./database/courses.db')
            with dbconn:
                cursor = dbconn.cursor()
                create_table_query = 'CREATE TABLE IF NOT EXISTS course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)'
                cursor.execute(create_table_query)
        except Exception:
            print('Unable to create Database !')

    def insert_data(self, data):
        try:
            with dbconn:
                cursor = dbconn.cursor()
                insert_query = 'INSERT INTO course(name, description, price, is_private) VALUES (?,?,?,?)'
                cursor.execute(insert_query, data)
                return True
        except Exception:
            print('Unable to insert data')
            return False

    def fetch_data(self):
        try:
            with dbconn:
                cursor = dbconn.cursor()
                fetch_query = 'SELECT * FROM course'
                cursor.execute(fetch_query)
                return cursor.fetchall()
        except Exception:
            print('Unable to fetch the data')
            return False

    def delete_data(self, id):
        try:
            with dbconn:
                cursor = dbconn.cursor()
                delete_query = 'DELETE FROM course WHERE id = ?'
                cursor.execute(delete_query, [id])
                return True
        except Exception:
            print('Unable to delete the data with id: ' + id)
            return False
