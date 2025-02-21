import turtle
import random


def draw_star(t, radius, color, line_thickness, num_lines):
    angle = 360 / num_lines
    t.color(color)
    t.width(line_thickness)
    for _ in range(num_lines):
        t.forward(radius)
        t.backward(radius)
        t.right(angle)


def randstar(num_stars):
    screen = turtle.Screen()
    screen.bgcolor("white")
    t = turtle.Turtle()
    t.speed(0)

    for _ in range(num_stars):
        # 随机位置
        x = random.randint(-300, 300)
        y = random.randint(-300, 300)
        t.penup()
        t.goto(x, y)
        t.pendown()

        # 随机属性
        radius = random.randint(50, 150)
        color = (random.random(), random.random(), random.random())
        line_thickness = random.randint(1, 5)
        num_lines = random.randint(5, 20)

        draw_star(t, radius, color, line_thickness, num_lines)

    # 关掉海龟
    t.hideturtle()
    screen.mainloop()


# 画图
if __name__ == '__main__':
    n = int(input('个数n='))
    randstar(n)