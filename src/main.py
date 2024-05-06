from user_acc import signup
from user_acc import login
# import user_acc // why can't do this?

# initial sign up, login or quit
print('********** Login System **********')
print('\n1.Signup')
print('2.Login')
# print("3.Exit")
ch = int(input('\nEnter your choice: '))
if ch == 1:
    signup()
elif ch == 2:
    login()
else:
    print('Invalid Choice!')


# 1. select vitamin to track
# 2. view history



# vitamin selection
print('\n********** Vitamin Selection **********')

# improve this list seleciton
vitamins =  [
    {1: '1. Fish Oil'},
    {2: '2. Magnesium'},
    {3: '3. Vitamin C'}
]
for vit in vitamins:
    print(list(vit.values()))

print('\nWhat would you like to track? Please enter your choice:')
# how to print text?