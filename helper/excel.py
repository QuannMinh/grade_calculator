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