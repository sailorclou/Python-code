import lx2_1
import lx2_2
import xlrd

def query_by_no(student_no, table):
    for i in range(len(table)):
        if str(student_no) == table[i][0]:
            return table[i]


if __name__ == '__main__':
    titles1, table1_data = lx2_1.read_xls(0)
    titles2, table2_data = lx2_1.read_xls(1)
    titles = titles2 + titles1[1:]
    table = lx2_2.table_merge(table1_data, table2_data)
    info = query_by_no(2351044, table)

    info_dict = dict(zip(titles, info))

    print(info_dict)