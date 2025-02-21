# 01 设计人员信息类
"""
包含属性：姓名（字符串），年龄（整数），工作（字符串）
提供一个方法，可查看个人信息
"""


class Person:
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job

    def check_info(self):
        print(f"个人信息 姓名：{self.name} 年龄：{self.age} 工作：{self.job}")


Tom = Person('Tom', 28, 'Teacher')
Person.check_info(Tom)


# 02 多态在程序设计中的使
class Hero:
    def __init__(self, name):
        self.name = name

    def skill_Q(self):
        pass

    def skill_W(self):
        pass

    def skill_E(self):
        pass

    def skill_R(self):
        pass


class Annie(Hero):
    def skill_Q(self):
        return f"{self.name}释放了Q技能，造成了伤害并晕眩敌人"

    def skill_W(self):
        return f"{self.name}释放了W技能，造成了伤害并降低敌人移动速度"

    def skill_E(self):
        return f"{self.name}释放了E技能，造成了伤害并施加火焰效果"

    def skill_R(self):
        return f"{self.name}释放了R技能，造成了大范围伤害并使敌人进入燃烧状态"


class Timo(Hero):
    def skill_Q(self):
        return f"{self.name}释放了Q技能，造成了伤害并减少敌人的护甲"

    def skill_W(self):
        return f"{self.name}释放了W技能，召唤了加里奥盾牌为他护卫"

    def skill_E(self):
        return f"{self.name}释放了E技能，施放了粘稠的蘑菇，使附近敌人减速"

    def skill_R(self):
        return f"{self.name}释放了R技能，召唤了天外陨石，对范围内的敌人造成巨额伤害"


# 测试
annie = Annie("安妮")
print(annie.skill_Q())
print(annie.skill_W())
print(annie.skill_E())
print(annie.skill_R())

timo = Timo("提莫")
print(timo.skill_Q())
print(timo.skill_W())
print(timo.skill_E())
print(timo.skill_R())


# 03 01增加出生日期
class Person:
    def __init__(self, name, age, job, birth):
        self.name = name
        self.age = age
        self.job = job
        self.birth = birth

    def check_info(self):
        input_birth = input("请输入出生日期××××.××.××")
        if input_birth == self.birth:
            print(f"个人信息 姓名：{self.name} 年龄：{self.age} 工作：{self.job}")
        else:
            print("输入错误，禁止访问")


Tom = Person('Tom', 28, 'Teacher', '2001.01.01')
Person.check_info(Tom)

# 04 编写一个数组类，重写加、减、乘法运算（均为对应位置的元素相加、减、乘）
class Array():
    def __init__(self, list0):  # 通过列表来建立数组
        self.data = list0

    def __add__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Arrays must have the same length for addition")
        result = [x + y for x, y in zip(self.data, other.data)]
        return Array(result)

    def __sub__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Arrays must have the same length for subtraction")
        result = [x - y for x, y in zip(self.data, other.data)]
        return Array(result)

    def __mul__(self, other):
        if len(self.data) != len(other.data):
            raise ValueError("Arrays must have the same length for multiplication")
        result = [x * y for x, y in zip(self.data, other.data)]
        return Array(result)


a = Array([1, 2, 3, 4])
b = Array([2, 4, 5, 6])
c = Array.__add__(a, b)
print(c)

