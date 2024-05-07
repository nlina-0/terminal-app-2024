import json
import csv

def vitamin_list():
    print('\n********** Vitamin Selection **********\n')
    print('\nWhat would you like to track? \n')
    vitamins = ['Fish Oil', 'Magnesium', 'Iron', 'Vitamin C', 'H2O']

    for key, value in enumerate(vitamins):
        print(f'{key + 1}. {value}')

#continue adding rest of list...
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


def add_to_user_file(date, vitamin, user_supp, user_rec_intake):
    user_data = {
        'date': date,
        'vitamin': vitamin,
        'supplement intake': user_supp,
        'reccomended intake': user_rec_intake
    }

    with open('user_data.csv', 'a') as f:
        fields = ['date', 'vitamin', 'supplement intake', 'reccomended intake']
        output_f = csv.DictWriter(f, fieldnames=fields)
        # output_f.writeheader()
        output_f.writerow(user_data)


def supplement_question(reccomended_intake):
    supp_ques = input('\nAre you taking any supplments (Y/N)? ')
    supp_ques_upper = supp_ques.upper()
    if supp_ques_upper == 'Y':
        # record into file
        user_supp_mg = int(input('How many mg are you taking daily? '))
        # add_to_user_file()
        if user_supp_mg >= reccomended_intake:
            print('You are taking a sufficent amount!')
        else:
            print('You are not taking a sufficent amount!')
            # grad reccomended foods from list
            print('Reccomended foods to increase vitamin intake: ...')
    elif supp_ques_upper == 'N':
        # grad reccomended foods from list
        print('Here are some reccomended foods to increase vitamin intake: ')
    else:
        print('Invalid Choice!')

    return user_supp_mg
