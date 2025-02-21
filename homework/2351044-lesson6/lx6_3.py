import pandas as pd
import numpy as np

class st_lesson:
    def __init__(self, st_no):
        self.st_no = st_no
        self.st_name = ""
        self.st_py = ""
        self.st_sex = ""
        self.st_course_list = []
        self.st_schedule_list = []

        # 读取 Excel 文件
        self.load_data()

    def load_data(self):
        # 读取sheet1
        df_info = pd.read_excel('xuanke.xls', sheet_name='信息')
        # 根据学号筛选数据
        st_info = df_info[df_info['学号'] == self.st_no].iloc[0]
        # 设置属性
        self.st_name = st_info['姓名']
        self.st_py = st_info['英文姓名']
        self.st_sex = st_info['性别']

        # 读取sheet2
        df_course = pd.read_excel('xuanke.xls', sheet_name='选课')
        student_course = df_course[df_course['学号'] == self.st_no].iloc[0]
        # 获取课程列表
        self.st_course_list = [course for course in student_course.index[1:] if student_course[course] == '√']

        # 读取sheet3
        schedule_df = pd.read_excel('xuanke.xls', sheet_name='上课时间')
        schedule_title = schedule_df.columns.tolist()
        schedule_list = schedule_df.values.tolist()
        self.st_schedule_list = [schedule_title] + schedule_list

    def display_schedule(self):
        # 显示课表
        print(f"学号：{self.st_no} 姓名：{self.st_name} 的课表")
        for row in self.st_schedule_list:
            print('\t'.join([str(cell).ljust(20) for cell in row]))

    def check_conflict(self):
        conflicts = []

        # 遍历每个时间段（跳过第一行标题）
        for row in self.st_schedule_list[1:]:
            time_slot = row[0]  # 获取时间段，例如 "上午一二节"
            # 遍历一周的每一天
            for day_idx in range(1, len(row)):
                courses = row[day_idx]  # 获取该时间段某天的课程
                if pd.notna(courses) and courses:  # 检查是否为 NaN 或空值
                    course_list = courses.split(',')  # 拆分课程列表
                    if len(course_list) > 1:  # 如果课程数量超过 1，说明存在冲突
                        conflict_detail = f"{time_slot} {self.st_schedule_list[0][day_idx]}{course_list}"
                        conflicts.append(conflict_detail)
        print(self.st_name, "的选课冲突有：")
        for item in conflicts:
            print(item)


# 示例使用
student = st_lesson(2351044)
student.display_schedule()
student.check_conflict()
