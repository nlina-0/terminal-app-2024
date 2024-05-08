import csv 

def signup():
    username = input('Create username: ')
    username_lower = username.lower()
    age = input('Age: ')
    sex = input('Male/Female: ')

    # appends the username, password, age and sex to users.csv file
    with open('user_acc.csv', 'a') as f:
        f.write(f'{username_lower},{age},{sex}\n')
    
    print('\n********** User Account **********')
    print(f'\nWelcome, {username.capitalize()}!')
    # user_index = stored_username.index(username)
    print(f'{age}, {sex.capitalize()}')

    return age, sex, username_lower


def login():
    while True:
        username = input('Enter username: ')
        username_lower = username.lower() 

        # list of usernames created from users.csv file
        stored_username = []
        stored_age = []
        stored_sex = []
        with open('user_acc.csv', newline='') as f:
            user_reader = csv.DictReader(f)
            # creates list of usernames from users.csv file and is stored into stored_username
            for row in user_reader:
                stored_username.append(row['username'])
                stored_age.append(row['age'])
                stored_sex.append(row['sex'])
        
        # print out user details
        if username_lower in stored_username:
            print('\n********** User Account **********')
            print(f'\nWelcome, {username.capitalize()}!')
            user_index = stored_username.index(username)
            print(f'{stored_age[user_index]}, {stored_sex[user_index].capitalize()}')
            return stored_age[user_index], stored_sex[user_index], username
        else:
            print('Invalid username')
