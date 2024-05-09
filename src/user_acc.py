import csv
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def signup():
    username = input('Create username: ')
    username_lower = username.lower()
    age = input('Age: ')

    # appends the username, password and age to users.csv file
    with open('user_acc.csv', 'a') as f:
        f.write(f'{username_lower},{age}\n')
    
    print('\n********** User Account **********')
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
                print(f'{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2')
                print('\033[39m')

        username = input(f'{Fore.CYAN}Enter username: ')
        print('\033[39m')
        username_lower = username.lower() 
        # list of usernames created from users.csv file
        stored_username = []
        stored_age = []
        with open('user_acc.csv', newline='') as f:
            user_reader = csv.DictReader(f)
            # creates list of usernames from users.csv file and is stored into stored_username
            for row in user_reader:
                stored_username.append(row['username'])
                stored_age.append(row['age'])
        
        # print out user details
        if username_lower in stored_username:
            print('\n********** User Account **********')
            user_index = stored_username.index(username)
            print(f'\nWelcome, {username.capitalize()}! {stored_age[user_index]}y.o\n')
            return stored_age[user_index], username
        else:
            print(f'{Fore.RED}{Style.BRIGHT}Invalid username')
            print('\033[39m')


