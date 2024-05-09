import sys
import csv
from datetime import datetime 
from user_acc import signup
from user_acc import login
from vitamins import vitamin_list
from vitamins import vitamin_select
from vitamins import vitamin_open_list
from vitamins import supplement_question
from operations import write_data
from operations import read_history

username = ''
user_age = 0

# initial sign up, login or quit
while True:
    print('********** Login System **********')
    print('\n1.Signup')
    print('2.Login')
    print('3.Exit')
    try:
        ch = int(input('\nEnter your choice: '))
        if ch == 1:
            login_age, login_username = signup()
            user_age += int(login_age)
            username += login_username
            break
        elif ch == 2:
            login_age, login_username = login()
            user_age += int(login_age)
            username += login_username
            break
        elif ch == 3:
            sys.exit("Goodbye, take care!")
        else:
            print('\nInvalid Choice! Please choose between 1, 2, 3\n')

    except ValueError:
        print('\nInvalid Choice! Please choose between 1, 2, 3\n')


# option to track new vitamin or view history
while True:
    print('\n********** Options **********')
    print('\n1.Select vitamin to track')
    print('2.View history') # view all or select date?
    print('3.Exit')
    try:
        ch2 = int(input('\nEnter your choice: '))
        if ch2 == 1:
            vitamin_list()
            user_vit_select = input('\nEnter the number: ')

            # prints out user selection based on list
            vit_select = vitamin_select(user_vit_select)
            
            # calls list of recommended daily intake of vitamins
            vit_reccomend_list_dict = vitamin_open_list()

            # defining the age selection
            age_select = ''
            if 19 <= user_age <= 50:
                age_select += '19to50'
            elif user_age >= 51:
                age_select += '51andup'
            elif user_age <= 18:
                age_select += '14to18'

            # opens list of vitamins
            vit_reccomend_list = vit_reccomend_list_dict[0]
            user_reccomended_intake = vit_reccomend_list[vit_select][age_select]

            # prints reccomended intake
            print(f'Your reccomended daily intake: {user_reccomended_intake}')

            # returns user supplement intake (mg) and if user met reccomended intake
            user_supp_mg, recc_met = supplement_question(user_reccomended_intake)

            # adds data to user file 
            current_date = datetime.now().strftime("%d/%m/%y")
            # checks to see if data already exists, asks user if they want to update existinf data, if no data exists then a new line is created
            write_data(username, current_date, vit_select, user_reccomended_intake, user_supp_mg, recc_met)

            input('\nPress enter to continue...')

        # view history 
        elif ch2 == 2:
            print('\n********** History **********')
            
            # reads user history
            read_history(username)

            input('\nPress enter to continue...')
        
        elif ch2 == 3:
            sys.exit("Goodbye, take care!")
        else:
            print('\nInvalid Choice! Please choose between 1, 2, 3\n')
    
    except ValueError:
        print('\nInvalid Choice! Please choose between 1, 2, 3\n')
