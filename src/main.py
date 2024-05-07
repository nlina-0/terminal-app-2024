from user_acc import signup
from user_acc import login
import sys
from vitamins import vitamin_list
from vitamins import vitamin_select
# from vitamins import vitamin_select
# import user_acc // why can't do this?


user_age = 0
user_sex = []

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


intake_list = []
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
        vitamin_select(user_vit_select)
        # vitamin_reccomend_intake()
        break
    elif ch2 == 2:
        pass
    elif ch2 == 3:
        sys.exit("Goodbye!")

