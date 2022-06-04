import csv
from csv import writer
import pandas as pd
from openpyxl import Workbook
from helper.utils import *


def create_workbook(title):
    workbook = Workbook()

    workbook['Sheet'].title = title
    sheet1 = workbook.active

    sheet1['A1'].value = 'Student Name'
    sheet1['B1'].value = 'Assignment'
    sheet1['C1'].value = 'Test'
    sheet1['D1'].value = 'Lab-Work'
    sheet1['E1'].value = 'GPA'
    return workbook, sheet1


def save_workbook(score, workbook, sheet1):
    final = []
    for student in score:
        result = []
        assignment = average_score(score[student]['assignment'])
        test = average_score(score[student]['test'])
        labwork = average_score(score[student]['lab-work'])
        gpa = average_gpa(assignment, test, labwork)
        result.extend([student, assignment, test, labwork, gpa])
        final.append(tuple(result))
    print(final)

    for i in final:
        sheet1.append(i)

    workbook.save("data/AverageGPA.xlsx")


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
                file_score = enter_score()
                calculate_grade(file_score)
                workbook, sheet1 = create_workbook('AverageGPA')
                save_workbook(file_score, workbook, sheet1)
            else:
                df = pd.read_excel('data/AverageGPA.xlsx')
                print(df)