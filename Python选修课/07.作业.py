
# 01 打印矩阵
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[1])):
            print(matrix[i][j], end=' ')
        print()
    return 0

'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print_matrix(matrix)


# 02 判断回文数
def is_palindrome(n):
    num_str = str(n)
    num_len = len(str(n))
    if num_len % 2 == 0:
        for i in range(int(num_len / 2)):
            if num_str[i] != num_str[num_len - 1 - i]:
                return False
        return True
    else:
        for i in range(int((num_len - 1) / 2)):
            if num_str[i] != num_str[num_len - 1 - i]:
                return False
        return True


n = int(input("请输入一个整数："))
is_palindrome(n)


# 03 计算行列式
def deternimant(matrix, det):
    n = len(matrix)
    if n == 1:
        det = matrix[0][0]
        return det

    for j in range(n):
        a = matrix[0][j]
        # 计算代数余子式
        sub_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        sign = (-1) ** j
        det += sign * a * deternimant(sub_matrix, det)
    return det


matrix = [[1, 2, 1], [1, 1, 1], [1, 0, 0]]
det = deternimant(matrix, 0)
print(det)

def determinant(matrix, det=0):
    n = len(matrix)
    if n == 1:
        det = matrix[0][0]
        return det

    for j in range(n):
        a = matrix[0][j]
        # 计算代数余子式
        sub_matrix = [row[:j] + row[j + 1:] for row in matrix[1:]]
        sign = (-1) ** j
        sub_det = determinant(sub_matrix)
        det += sign * a * sub_det
    return det


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
det = determinant(matrix)
print(det)


def a(b, c=1):
    b = b + 2
    c = 2
    a(1)
    return c

d = a(1)
print(d)
'''

# 04 矩阵相乘
def matmul(matrix_a, matrix_b):
    matrix = [[0 for _ in range(len(matrix_b))] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a[0])):
            for k in range(len(matrix_b[0])):
                matrix[i][j] = matrix_a[i][k] * matrix_b[k][j]
    print_matrix(matrix)
    return


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matmul(a, b)
