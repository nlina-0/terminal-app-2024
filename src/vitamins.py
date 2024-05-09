import json
import csv

def vitamin_list():
    print('\n********** Vitamin Selection **********\n')
    print('\nWhat would you like to track? \n')
    vitamins = ['Fish Oil', 'Magnesium', 'Vitamin D', 'B12']

    for key, value in enumerate(vitamins):
        print(f'{key + 1}. {value}')

def vitamin_select(x):
    match x:
        case '1':
            print('\n********** Fish Oil ********** \n')
            print('unit: mg')
            return 'fish oil'
        case '2':
            print('\n********** Magnesium ********** \n')
            print('unit: mg')
            return 'magnesium'
        case '3':
            print('\n********** Vitamin D ********** \n')
            print('unit: IU')
            return 'vitamin d'
        case '4':
            print('\n********** B12 ********** \n')
            print('unit: mcg')
            return 'b12'
    

def vitamin_open_list():
    intake_list = []
    
    with open('vitamins_list.json') as f:
        reccomended_intake_list = json.load(f)
        intake_list.append(reccomended_intake_list)

    return intake_list

def supplement_question(reccomended_intake):
    # do i need to add error handling here?
    supp_ques = input('\nAre you taking any supplments? [y/n]: ')
    supp_ques_upper = supp_ques.upper()
    if supp_ques_upper == 'Y':
        # record into file
        # its not always mg though
        user_supp_mg = int(input('How much are you taking daily? '))
        # add_to_user_file()
        if user_supp_mg >= reccomended_intake:
            print('You are taking a sufficent amount!')
            recc_met = 'Yes :)'
            return user_supp_mg, recc_met
        else:
            print('You are not taking a sufficent amount!')
            # grad reccomended foods from list
            print('Reccomended foods to increase vitamin intake: ...')
            recc_met = 'No :('
            return user_supp_mg, recc_met
    elif supp_ques_upper == 'N':
        user_supp_mg = 0
        recc_met = 'Unsure, no supplments were recorded :/'
        # grad reccomended foods from list
        print('Here are some reccomended foods to increase vitamin intake: ')
        return user_supp_mg, recc_met

    else:
        print('Invalid Choice!')

    
def call_recommended_foods():
    pass