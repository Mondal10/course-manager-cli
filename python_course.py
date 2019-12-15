import sqlite3 as lite


# Functionality Here
class DatabaseManagement(object):

    def __init__(self):
        global dbconn
        try:
            dbconn = lite.connect('courses.db')
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

# User Interface Here


def main():
    print('#' * 40)
    print('\n \t:: COURSE MANAGEMENT :: \n')
    print('#' * 40)
    print('\n')

    db = DatabaseManagement()

    print('#' * 40)
    print('\n \t:: USER MANUAL :: \n')
    print('#' * 40)
    print('\n')

    print('Press 0 to Exit\n')
    print('Press 1 to Insert a new course\n')
    print('Press 2 to Show all courses\n')
    print('Press 3 to Delete a course with ID\n')

    print('_' * 40)
    print('\n')

    choice = input('\n Enter a choice: ')

    if choice == '1':
        name = input('\n Enter a name: ')
        description = input('\n Enter a description: ')
        price = input('\n Enter a price: ')
        is_private = input('\n Is this course private (0/1): ')

        if db.insert_data([name, description, price, is_private]):
            print('\n Course was inserted successfully')
        else:
            print('\n Oops something went wrong!')

    elif choice == '2':
        print('\n \t:: Course List :: \n')
        print('_' * 40)
        print('\n')

        for index, course in enumerate(db.fetch_data()):
            print('\n Serial No.: ' + str(index + 1))
            print('\n Course ID: ' + str(course[0]))
            print('\n Course Name: ' + str(course[1]))
            print('\n Course Description: ' + str(course[2]))
            print('\n Course Price: ' + str(course[3]))

            private = 'Yes' if course[4] else 'No'
            print('\n Is Course Private: ' + private)
            print('_' * 40)

    elif choice == '3':
        delete_id = input('Enter course ID you want to delete: ')

        if db.delete_data(delete_id):
            print('Course was deleted with ID ' + delete_id)
        else:
            print('Could not delete the course with ID ' + delete_id)

    else:
        print('\n No such choice available')


if __name__ == '__main__':
    main()
