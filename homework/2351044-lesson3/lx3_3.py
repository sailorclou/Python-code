import json

def load_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def search_data(data, keyword):
    results = []
    for student in data:
        if (keyword in str(student['学号']) or
            keyword in student['姓名'] or
            keyword in student['英文姓名'] or
            keyword in student['性别']):
            results.append(student)
    return results

def main():
    filename = 'course.txt'
    data = load_data(filename)

    keyword = input("请输入要搜索的关键字：")

    results = search_data(data, keyword)
    print(f"共找到{len(results)}条数据：")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
