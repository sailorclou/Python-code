import json

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def find_score(data, student_id, course_name):
    for student in data:
        if student['学号'] == student_id:
            for score in student['score']:
                if course_name in score:
                    return score[course_name]
    return None

def main():
    filename = 'course.txt'
    data = load_data(filename)
    while(1):
        student_id = input("请输入学号: ")
        course_name = input("请输入课程名称：")

        score = find_score(data, student_id, course_name)
        if score != "":
            print(f"{student_id} 的 {course_name} 成绩为: {score}")
        else:
            print(f"该学号对应的{course_name}成绩没找到")

        print()

if __name__ == "__main__":
    main()
