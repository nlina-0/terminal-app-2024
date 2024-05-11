import csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def signup():
    username = input('Create username: ')
    username_lower = username.lower()
    
    while True:
        try:
            age = int(input('Age: '))
            break
        except ValueError:
            print(f'{Fore.RED}Age must be a valid integer. Please try again.')

    # Appends the username, password and age to users.csv file
    with open('user_acc.csv', 'a') as f:
        f.write(f'{username_lower},{age}\n')
    
    # print('\n********** User Account **********')
    print(f'\nWelcome, {username.capitalize()}! {age}y.o')

    return age, username_lower


def login():
    while True:
        while True:
            print(f'1.Enter username \n2.Return to main menu')
            choice = input(f'\n{Fore.CYAN}Enter your choice: ')
            print('\033[39m')
            if choice == '1':
                break
            if choice == '2':
                return None
            else:  
                print(f'{Fore.RED}Invalid Choice! Please choose between 1, 2')
                print('\033[39m')

        username = input('Username: ')
        username_lower = username.lower() 
        # List of usernames created from users.csv file
        stored_username = []
        stored_age = []
        with open('user_acc.csv', newline='') as f:
            user_reader = csv.DictReader(f)
            # Creates list of usernames from users.csv file and is stored into stored_username
            for row in user_reader:
                stored_username.append(row['username'])
                stored_age.append(row['age'])
        
        # Print out user details
        if username_lower in stored_username:
            print('\n********** User Account **********')
            user_index = stored_username.index(username)
            print(f'\nWelcome, {username.capitalize()}! {stored_age[user_index]}y.o\n')
            return stored_age[user_index], username
        else:
            print(f'{Fore.RED}Invalid username')
            print('\033[39m')


