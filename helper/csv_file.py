from helper.utils import *
import csv


def append_score(score):
    final = []
    for student in score:
        result = []
        assignment = average_score(score[student]['assignment'])
        test = average_score(score[student]['test'])
        labwork = average_score(score[student]['lab-work'])
        gpa = average_gpa(assignment, test, labwork)
        result.extend([student, assignment, test, labwork, gpa])

    with open('data/score.csv', 'a', newline="") as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(result)