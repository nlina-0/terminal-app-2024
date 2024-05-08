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

    with open('user_data.csv', 'a') as f:
        fields = ['user', 'date', 'vitamin', 'supplement intake', 'recommended intake', 'recommended met']
        output_f = csv.DictWriter(f, fieldnames=fields)
        # output_f.writeheader()
        output_f.writerow(user_data)