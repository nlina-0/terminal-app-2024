import json

def vitamin_list():
    print('\n********** Vitamin Selection **********\n')
    print('\nWhat would you like to track? \n')
    vitamins = ['Fish Oil', 'Magnesium', 'Iron', 'Vitamin C', 'H2O']

    for key, value in enumerate(vitamins):
        print(f'{key + 1}. {value}')


def vitamin_select(x):
    match x:
        case '1':
            print('\n********** Fish Oil ********** \n')
            return 'fish oil'
        case '2':
            print('\n********** Magnesium ********** \n')
            return 'magnesium'
    

def vitamin_list_sex(y):
    intake_list = []
    
    if y == 'female':
        with open('vitamins_female.json') as f:
            reccomended_intake_list = json.load(f)
            intake_list.append(reccomended_intake_list)
    elif y == 'male':
        pass

    return intake_list

    # input('\nAre you taking any supplments (Y/N)? ')
    # input('How many mg are you taking daily? ')


def supplement_question():
    supp_ques = input('\nAre you taking any supplments (Y/N)? ')
    if supp_ques == 'Y':
        supp_mg = int(input('How many mg are you taking daily? '))
        #append to list or file
    elif supp_ques == 'N':
        print('Here are some reccomended foods to increase vitamin intake for vitamin: ')
        pass
    else:
        print('Invalid Choice!')

