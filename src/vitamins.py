import json
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def vitamin_list():
    print('\n********** Vitamin Selection **********\n')
    print('\nWhat would you like to track? \n')
    vitamins = [
        'Fish Oil',
        'Magnesium',
        'Vitamin D',
        'B12'
        ]
    for key, value in enumerate(vitamins):
        print(f'{key + 1}. {value}')

def vitamin_select(x):
    # add expectation here...KeyError caused
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
        case _:
            print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between 1, 2, 3, 4\n')
    

def vitamin_open_list():
    intake_list = []
    
    with open('vitamins_list.json') as f:
        reccomended_intake_list = json.load(f)
        intake_list.append(reccomended_intake_list)

    return intake_list

def supplement_question(reccomended_intake):
    while True:
        try:
            supp_ques = input('\nAre you taking any supplments? [y/n]: ')
            supp_ques_upper = supp_ques.upper()
            if supp_ques_upper == 'Y':
                user_supp_mg = int(input('How much are you taking daily? '))
                
                # add_to_user_file()
                if user_supp_mg >= reccomended_intake:
                    print(f'{Fore.GREEN}You are taking a sufficent amount!')
                    recc_met = 'Yes :)'
                    return user_supp_mg, recc_met
                
                else:
                    print(f'{Fore.YELLOW}You are not taking a sufficent amount!')
                    # print('Reccomended foods to increase vitamin intake: ...')
                    recc_met = 'No :('
                    return user_supp_mg, recc_met
            
            elif supp_ques_upper == 'N':
                user_supp_mg = 0
                recc_met = 'Unsure, no supplments were recorded :/'
                # print('Here are some reccomended foods to increase vitamin intake: ')
                return user_supp_mg, recc_met
            
            else:
                print(f'{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between y or n\n')
        
        except (ValueError, TypeError, KeyError):
            print(f'\n{Fore.RED}{Style.BRIGHT}Invalid Choice! Please choose between y or n\n')