# 打印菱形
# def diamond(n, m):
#     for i in range(n):
#         # 上部分
#         for j in range(m):
#             print(" " * (m - j - 1) + '*' * (2 * j + 1))
#         # 下部分
#         for j in range(m - 1, -1, -1):
#             print(" " * (m - j - 1) + '*' * (2 * j + 1))
#
#
# diamond(2, 3)


def diamond(n, m):
    for i in range(1, n + 1):
        for j in range(1, 2 * m):
            s1 = ' ' * abs(j - m)
            s2 = '*' * (2 * (m - abs(j - m)) - 1)
            print(s1+s2)


if __name__ == '__main__':
    n = int(input('n='))
    m = int(input('m='))
    diamond(n, m)