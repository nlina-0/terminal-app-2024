import sys
from datetime import datetime 
from user_acc import signup
from user_acc import login
from vitamins import vitamin_list
from vitamins import vitamin_select
from vitamins import vitamin_list_sex
from vitamins import supplement_question
from vitamins import add_to_user_file

# username = ''
user_age = 0
user_sex = ''
# current_reccomended_user_intake = 0

# initial sign up, login or quit
while True:
    print('********** Login System **********')
    print('\n1.Signup')
    print('2.Login')
    print('3.Exit')
    ch = int(input('\nEnter your choice: '))
    if ch == 1:
        signup()
        break
    elif ch == 2:
        login_age, login_sex = login()
        user_age += int(login_age)
        user_sex += login_sex
        break
    elif ch == 3:
        sys.exit("Goodbye!")
    else:
        print('Invalid Choice!')


# intake_list = []
# option to track new vitamin or view history
while True:
    print('\n********** Options **********')
    print('\n1.Select vitamin to track')
    # select a date or view all
    print('2.View history') 
    print('3.Exit')
    ch2 = int(input('\nEnter your choice: '))

    if ch2 == 1:
        vitamin_list()
        user_vit_select = input('\nEnter the number: ')

        # prints out user selection based on list
        vit_select = vitamin_select(user_vit_select)
        
        # calls list of vitamins based on male/female and prints out list
        vit_reccomend_list_dict = vitamin_list_sex(user_sex)

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
        # current_reccomended_user_intake += user_reccomended_intake

        # prints reccomended intake
        print(f'Your reccomended daily intake: {user_reccomended_intake}mg')

        # returns user_supp_mg
        user_supp_mg = supplement_question(user_reccomended_intake)

        current_date = datetime.now().strftime("%d/%m/%y")
        add_to_user_file(current_date, vit_select, user_supp_mg, user_reccomended_intake)

        input('\nPress enter to continue...')

    # view history 
    elif ch2 == 2:
        pass
    elif ch2 == 3:
        sys.exit("Goodbye!")

