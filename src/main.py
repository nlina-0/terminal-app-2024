import sys
from datetime import datetime 
import user_acc
import vitamins 
import operations
import colorama
from colorama import Fore, Style
colorama.init(autoreset=True)


username = ''
user_age = 0

# Sign up, login or quit
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


# Options menu, select vitamin to track, view history or exit
while True:
    print('\n********** Options **********')
    print('\n1.Select vitamin to track')
    print('2.View history')
    print('3.Exit')
    try:
        ch2 = int(input(f'\n{Fore.CYAN}Enter your choice: '))
        print('\033[39m')
        if ch2 == 1:
            # Vitamin selection list. Prints out list of vitamins and stores user selection to a variable
            vitamin_ch = vitamins.vitamin_list()

            # Prints out heading of vitamin user selected. Store name of vitamin into variable to be used later to identify correct recommendations.
            vit_select = vitamins.vitamin_select(vitamin_ch)
            
            # Reads list of recommended daily intake of vitamins and stores it into variable
            vit_reccomend_list_dict = vitamins.vitamin_open_list()

            # Defining the age bracket to select the correct reccomendation from vitamins_list
            age_select = ''
            if 19 <= user_age <= 50:
                age_select += '19to50'
            elif user_age >= 51:
                age_select += '51andup'
            elif user_age <= 18:
                age_select += '14to18'

            # Reads and prints recommended intake
            vit_reccomend_list = vit_reccomend_list_dict[0]
            user_reccomended_intake = vit_reccomend_list[vit_select][age_select]
            print(f'Your reccomended daily intake: {user_reccomended_intake}')

            # Returns user supplement intake and if user has met reccomended intake
            user_supp_mg, recc_met = vitamins.supplement_question(user_reccomended_intake)

            # Gets todays date 
            current_date = datetime.now().strftime("%d/%m/%y")
            # Checks to see if data already exists, asks user if they want to update existing data, if no data exists then a new line is created in user_data.csv
            operations.write_data(username, current_date, vit_select, user_reccomended_intake, user_supp_mg, recc_met)

            input('\nPress enter to continue...')

        # View history 
        elif ch2 == 2:
            print('\n********** History **********')
            operations.read_history(username)
            input('\nPress enter to continue...')

        elif ch2 == 3:
            sys.exit(f'Goodbye, take care!')

        else:
            print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3\n')
    
    except (ValueError, TypeError, KeyError):
        print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3\n')
