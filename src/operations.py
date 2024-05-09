import csv

def read_history(username):
    with open('user_data.csv', 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                if row['user'] == username:
                    print(f'User: {row["user"].capitalize()}')
                    print(f'Date: {row["date"]}')
                    print(f'Vitamin: {row["vitamin"].title()}')
                    print(f'Recommended Intake: {row["recommended intake"]}')
                    print(f'Supplement Intake: {row["supplement intake"]}')
                    print(f'Recommended Met: {row["recommended met"]}')
                    print() 

# overwrites existing data
def write_data(name, date, vitamin, user_rec_intake, user_supp=0, recommended_met=0):
    updated = False
    user_data = {
        'user': name,
        'date': date,
        'vitamin': vitamin,
        'supplement intake': user_supp,
        'recommended intake': user_rec_intake,
        'recommended met': recommended_met
    }
    new_data = {
        'supplement intake': user_supp,
        'recommended intake': user_rec_intake,
        'recommended met': recommended_met
    }

    # read all data from the CSV file into memory
    with open('user_data.csv', 'r') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

        # iterate over the data and identify the row to update
        for row in rows:
            if row['user'] == name and row['date'] == date and row['vitamin'] == vitamin:
                # ask user if they want to update:
                print('\n********** Record Exists **********')
                print(f'\nData for {vitamin.title()} on {date} already exists!')
                print("Supplement Intake:", row['supplement intake'])
                print("Recommended Met:", row['recommended met'])
                overwrite = input('\nDo you want to overwrite? [y/n]: ')

                if overwrite.lower() == 'y':
                    print('\n********** Record Updated **********')
                    print(f'\nData for {vitamin.title()} on {date} updated!')
                    row.update(new_data)
                    updated = True
                    break
                else: 
                    print('\n********** Record Not Updated **********')
                    print(f'\nData for {vitamin.title()} on {date} not updated!')
                    return
        
        # re-writes data with updated data
        with open('user_data.csv', 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        
        if not updated:
            with open('user_data.csv', 'a') as f:
                fields = ['user', 'date', 'vitamin', 'supplement intake', 'recommended intake', 'recommended met']
                output_f = csv.DictWriter(f, fieldnames=fields)
                output_f.writerow(user_data)