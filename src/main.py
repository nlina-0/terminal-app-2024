import sys
from datetime import datetime 
import user_acc
import vitamins 
import operations
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


username = ''
user_age = 0

# initial sign up, login or quit
while True:
    print('\n********** Login System **********')
    print('\n1.Signup')
    print('2.Login')
    print('3.Exit')
    try:
        ch = int(input(f'\n{Fore.CYAN}Enter your choice: '))
        print('\033[39m') # resets color
        if ch == 1:
            login_age, login_username = user_acc.signup()
            user_age += int(login_age)
            username += login_username
            break
        elif ch == 2:
            login_details = user_acc.login()
            if login_details is None:
                continue 
            else:
                login_age, login_username = login_details
                user_age += int(login_age)
                username += login_username
                break
        elif ch == 3:
            sys.exit('Goodbye, take care!\n')
        else:
            print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3\n')
    except ValueError:
        print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3\n')


# option to track new vitamin or view history
while True:
    print('********** Options **********')
    print('\n1.Select vitamin to track')
    print('2.View history') # view all or select date?
    print('3.Exit')
    try:
        ch2 = int(input(f'\n{Fore.CYAN}Enter your choice: '))
        print('\033[39m')
        if ch2 == 1:
            # prints out list of vitamins
            vitamins.vitamin_list()
            user_vit_select = input(f'\n{Fore.CYAN}Enter the number: ')
            print('\033[39m')

            # prints out heading of vitamin user selected. Stored into variable to be used later to identify correct recommendations
            vit_select = vitamins.vitamin_select(user_vit_select)
            
            # calls list of recommended daily intake of vitamins and stores it into variable
            vit_reccomend_list_dict = vitamins.vitamin_open_list()

            # defining the age selection
            age_select = ''
            if 19 <= user_age <= 50:
                age_select += '19to50'
            elif user_age >= 51:
                age_select += '51andup'
            elif user_age <= 18:
                age_select += '14to18'

            # reads from file that contains vitamins and recommended intake. Uses users vitamin selection and age to print out the recommended intake. 
            vit_reccomend_list = vit_reccomend_list_dict[0]
            user_reccomended_intake = vit_reccomend_list[vit_select][age_select]
            print(f'Your reccomended daily intake: {user_reccomended_intake}')

            # returns user supplement intake and if user has met reccomended intake
            user_supp_mg, recc_met = vitamins.supplement_question(user_reccomended_intake)

            # gets todays date 
            current_date = datetime.now().strftime("%d/%m/%y")
            # checks to see if data already exists, asks user if they want to update existing data, if no data exists then a new line is created in .csv file
            operations.write_data(username, current_date, vit_select, user_reccomended_intake, user_supp_mg, recc_met)

            input('\nPress enter to continue...')

        # view history 
        elif ch2 == 2:
            print('\n********** History **********')
            # reads user history
            operations.read_history(username)
            input('\nPress enter to continue...')

        elif ch2 == 3:
            sys.exit(f'Goodbye, take care!')

        else:
            print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3\n')
    
    except ValueError:
        print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3\n')
