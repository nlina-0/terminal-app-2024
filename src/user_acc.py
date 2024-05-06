import csv 

def signup():
    username = input('Create username: ')
    username_lower = username.lower()
    age = input('Age: ')
    sex = input('Male/Female: ')

    # appends the username, password, age and sex to users.csv file
    with open('users.csv', 'a') as f:
        f.write(f'{username_lower},{age},{sex}\n')

def login():
    username = input('Enter username: ')
    username_lower = username.lower() 

    # list of usernames created from users.csv file
    stored_username = []
    with open('users.csv', newline='') as f:
        user_reader = csv.DictReader(f)
        # creates list of usernames from users.csv file and is stored into stored_username
        for row in user_reader:
            stored_username.append(row['username'])
    
    # print out user details
    if username_lower in stored_username:
        print('\n********** User Account **********')
        print(f'\nWelcome, {username.capitalize()}!')
        print(f'23, Male (example)')
    else:
        print('Invalid username')

def vitamin_select():
    pass