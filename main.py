from helper.csv_file import *
from csv import writer

print('--------------------------GRADE CALCULATOR--------------------------')
print('Do you have an account or not? ')
inp = input('PLease enter yes or no: ').lower()

if inp == 'no':
    data_list = []
    username = input('Please sign up username: ')
    password = input('Please sign up password: ')
    role = input('Are you teacher or parent: ')
    data_list.extend([username, password, role])

    with open('data/username.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)

        with open('data/username.csv', 'a', newline='') as new_file:
            writer_object = writer(new_file)
            writer_object.writerow(data_list)
            new_file.close()

            for line in csv_reader:
                if data_list == list(line):
                    print('Found!')
                    break
                else:
                    print('----------SUCCESSFULLY SIGNED UP----------')
                    break

print('-------------PLEASE LOGIN-------------')
username1 = input('Please enter username: ')
password1 = input('Please enter password: ')
role1 = input('Are you teacher or parent: ')

with open('data/username.csv', 'r') as csv_file:
    csv_login = csv.reader(csv_file)

    for line in csv_login:
        if list(line)[0] == username1 and list(line)[1] == password1 and list(line)[2] == role1:
            print('Loading......SUCCESSFULLY LOGIN')
            if role1 == 'teacher':
                # check them diem
                file_score = enter_score()
                calculate_grade(file_score)
                append_score(file_score)
            else:
                with open('data/score.csv', 'r') as csv_file:
                    csv_reader = csv.reader(csv_file)  # Read the original csv_file
                    print('You are able to view score only!')

                    children_check = input('Please enter name of your child: ')

                    for line in csv_reader:
                        if children_check in line:
                            print(line)