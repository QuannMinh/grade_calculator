# Loop qua key của dictionary mẹ tên là score --> Lấy ra điểm điểm trung bình của assignment
# test và lab-work --> Print ra kết quả gpa lấy đến số thập phân thứ nhất
def calculate_grade(dictionary):
    for i in dictionary.keys():
        average_assignment = average_score(dictionary[i]['assignment'])
        average_test = average_score(dictionary[i]['test'])
        average_labwork = average_score(dictionary[i]['lab-work'])
        gpa = round(average_gpa(average_assignment, average_test, average_labwork), 1)
        return gpa


def average_gpa(a, b, c):
    gpa = (a + (b * 7) + (c * 2)) / 10
    return gpa


def average_score(lst):
    counter = 0
    summ = 0
    for i in lst:
        summ = summ + i
        counter = counter + 1

    average = summ / counter
    return average


# Thêm các điểm vào 1 list vào 1 dictionary dựa vào key là loại điểm và value là số điểm
def update_dict(result, option):
    number = int(input(f"Enter number of {option}: "))
    grade_list = []
    for i in range(number):
        grade = int(input(f"Enter score: "))
        grade_list.append(grade)
    result[option] = grade_list
    return result


def enter_score():
    score = {}
    # Nhập vào số người --> Để tạo bằng đấy số vòng loop
    while True:
        try:
            people = int(input("Please enter number of people: "))
            break
        except ValueError:
            print("No valid integer! Please try again ...")

    # Loop qua bằng số người nhập vào
    for i in range(people):
        # Mỗi lần loop nhập vào tên học sinh = key
        name = input("Enter a name: ").title()  # Return a string where the first character in every word is upper case
        result = {}
        # update điểm của asignment vào dictionary con tên là result của dictionary mẹ tên là score
        result = update_dict(result, 'assignment')
        # update điểm của test vào dictionary con tên là result của dictionary mẹ tên là score
        result = update_dict(result, 'test')
        # update điểm của lab_work vào dictionary con tên là result của dictionary mẹ tên là score
        result = update_dict(result, 'lab-work')
        # Thêm key là tên học sinh và value là result vào dictionary tên là score
        score[name] = result

    return score