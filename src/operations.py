import csv

def write_to_file(user, date, vitamin, user_rec_intake, user_supp=0, recommended_met=0):
    user_data = {
        'user': user,
        'date': date,
        'vitamin': vitamin,
        'supplement intake': user_supp,
        'recommended intake': user_rec_intake,
        'recommended met': recommended_met
    }

    # check existing data
    with open('user_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['user'] == user and row['date'] == date and row['vitamin'] == vitamin:
                print('\n********** Record Exists **********')
                print(f'\nData for {vitamin.title()} on {date} already exists!')
                print("Supplement Intake:", row['supplement intake'])
                print("Recommended Met:", row['recommended met'])

                # ask user if they want to overwrite existing data
                overwrite = input('\nDo you want to overwrite? [y/n]: ')
                if overwrite.lower() == 'y':
                    print('\n********** Record Updated **********')
                    print(f'\nData for {vitamin.title()} on {date} updated!')

                    # update existing data
                    with open('user_data.csv', 'a') as f:
                        fields = ['user', 'date', 'vitamin', 'supplement intake', 'recommended intake', 'recommended met']
                        output_f = csv.DictWriter(f, fieldnames=fields)
                        output_f.writerow(user_data)
                    break

                else:
                    print('\n********** Record Not Updated **********')
                    print(f'\nData for {vitamin.title()} on {date} not updated!')
                    break
            else:
                # this is written twice - not good
                with open('user_data.csv', 'a') as f:
                    fields = ['user', 'date', 'vitamin', 'supplement intake', 'recommended intake', 'recommended met']
                    output_f = csv.DictWriter(f, fieldnames=fields)
                    output_f.writerow(user_data)
                break