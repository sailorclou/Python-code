import xlrd
import json

def read_xls(sh):
    work_book = xlrd.open_workbook('score.xls')
    work_sheet = work_book.sheets()[sh]
    sheet_titles = work_sheet.row_values(0)

    sheet_data = []
    n_rows = work_sheet.nrows
    for i in range(1, n_rows):
        sheet_data.append(work_sheet.row_values(i))

    return sheet_titles, sheet_data


def table_merge(list_1, list_2):
    table = []
    for i in range(len(list_2)):
        table.append(list_2[i])
        id = str(list_2[i][0])
        for item in list_1:
            if id == item[0]:
                table[i] = table[i] + item[1:]

    return table

def list_to_dict(i, table, titles1, titles2):
    info = {}
    info.update(dict(zip(titles2, table[i][0:4])))
    dict21 = dict(zip(titles1[1:], table[i][4:10]))
    dict22 = dict(zip(titles1[1:], table[i][10:]))
    info['score'] = []
    info['score'].append(dict21)
    info['score'].append(dict22)

    return info



if __name__ == '__main__':
    titles1, table1_data = read_xls(0)
    titles2, table2_data = read_xls(1)
    titles = titles2 + titles1[1:] + titles1[1:]
    table = table_merge(table1_data, table2_data)
    # print(titles1)
    # print(table)
    # print(len(table))
    # print()
    all_info = []

    for i in range(len(table)):
        info = list_to_dict(i, table, titles1, titles2)
        all_info.append(info)

    # print(all_info)

    with open("./course.txt", "w", encoding='utf-8') as json_file:
        json.dump(all_info, json_file, ensure_ascii=False, indent=3)
