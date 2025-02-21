import xlrd


def read_xls(sh):
    work_book = xlrd.open_workbook('score.xls')
    work_sheet = work_book.sheets()[sh]
    sheet_titles = work_sheet.row_values(0)

    sheet_data = []
    n_rows = work_sheet.nrows
    for i in range(1, n_rows):
        sheet_data.append(work_sheet.row_values(i))

    return sheet_titles, sheet_data


if __name__ == '__main__':
    sheet_titles, sheet_data = read_xls(0)
    print(sheet_titles)
    print(sheet_data)
    sheet_titles, sheet_data = read_xls(1)
    print(sheet_titles)
    print(sheet_data)