from DatabaseManagement import DatabaseOperations
# User Interface Here


def create():
    print('#' * 40)
    print('\n \t:: COURSE MANAGEMENT :: \n')
    print('#' * 40)
    print('\n')

    db = DatabaseOperations()

    while True:
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

        elif choice == '0':
            print(':::::EXITING:::::')
            break

        else:
            print('\n No such choice available')
