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
            return "fish oil"
            print('Reccomended daily intake: ')
            # vitamin_questions()
        case '2':
            print('\n********** Magnesium ********** \n')
            # vitamin_questions()
    
    # return x - already stored in user_vitamin_select


# user_vitamin_select = input('\nEnter the number: ')
# vitamin_select(user_vitamin_select)

user_sex = 'female'
user_age = 23

def vitamin_reccomend_intake():
    
    if user_sex == 'female':
        with open('vitamins_female.json') as f:
            reccomended_intake_list = json.load(f)
            intake_list += reccomended_intake_list
            # if user_age >= 19 and user_age <= 50:
            #     age_select = 1
            # elif user_age >= 51:
            #     age_select = 2
            # else:
            #     age_select = 0
            # reccomended_intake = reccomended_intake_list[user_vit_select][age_select]



        #if user sex is female, open female vitamin file
        #select vitamn based on user_vitamin_select (eg, 1 for fish oil)
        #if user age is between 19 - 50, select value of vitman
        #return value into print statment or store into reccomend_intake

        # print('Your reccomended daily intake: ')

    # with open('vitamins_female.json') as f:
    #     vitfemale = json.load(f)
        # print(vitfemale[0]["19 to 50"])

    # input('\nAre you taking any supplments (Y/N)? ')
    # input('How many mg are you taking daily? ')

