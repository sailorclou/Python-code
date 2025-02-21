def tablem(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            num = i * j
            print(f'{num:4}', end=' ')
        print()


if __name__ == '__main__':
    n = int(input('n='))
    tablem(n)
