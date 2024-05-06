from user_acc import signup
from user_acc import login
import sys
from vitamins import vitamin_list
# import user_acc // why can't do this?

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
        login()
        break
    elif ch == 3:
        sys.exit("Goodbye!")
    else:
        print('Invalid Choice!')


# option to track new vitamin or view history
print('\n********** Options **********')
print('\n1.Select vitamin to track')
# select a date or view all
print('2.View history') 
print('3.Exit')
ch2 = int(input('\nEnter your choice: '))
if ch2 == 1:
    # output vitamin selection
    vitamin_list()
elif ch2 == 2:
    pass
elif ch2 == 3:
    sys.exit("Goodbye!")

