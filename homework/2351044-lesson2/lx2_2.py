import lx2_1
import xlrd


def table_merge(list_1, list_2):
    for i in range(len(list_1)):
        list_1[i][0] = str(list_1[i][0])
        id = str(list_1[i][0])
        for item in list_2:
            if id == item[0]:
                list_1[i] = item + list_1[i][1:]
    return list_1


if __name__ == '__main__':
    _, table1_data = lx2_1.read_xls(0)
    _, table2_data = lx2_1.read_xls(1)
    table = table_merge(table1_data, table2_data)
    print(table)

