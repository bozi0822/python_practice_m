import xlrd
import re
import xlwt
import os
from icecream import ic
from openpyxl import *


def get_file_from_fold(_path):
    files = os.listdir(_path)
    files_list = []
    for filename in files:
        if not (filename.__contains__('.xls') or filename.__contains__('.xlsx')):
            continue
        files_list.append(_path + filename)
    return files_list


class Excel_reader:
    """excel读取类"""
    _a_list = []
    _head_list = []

    def __init__(self, _file_name, _sheet_idx):
        self.file = _file_name
        self.wb = load_workbook(self.file, data_only=True)
        sheets = self.wb.sheetnames
        self.sheet = sheets[0]
        self.ws = self.wb[self.sheet]
        self.row_sum, self.col_sum = self.get_row_col_sum()

    def get_sheet(self):
        """
        获取表
        :return:
        """
        # 获取所有sheet的名字
        sheet_names = self.wb.sheetnames
        name = self.file
        str_list = name.split('\\')  # 截取生成表名
        for sheet_name in sheet_names:
            print('文件名：' + str_list[len(str_list) - 1] + ':\n表名：', sheet_name)
        # sheet1索引从0开始，得到sheet1表
        sheet = sheet_names[0]
        return sheet

    # 获取表格的总行数和总列数
    def get_row_col_sum(self):
        rows = self.ws.max_row
        columns = self.ws.max_column
        return rows, columns

    # 获取某个单元格的值
    def get_cell_value(self, row, column):
        cell_value = self.ws.cell(row=row, column=column).value
        return cell_value

    # 获取某列的所有值
    def get_col_value(self, column):
        rows = self.ws.max_row
        column_data = []
        for i in range(1, rows + 1):
            cell_value = self.ws.cell(row=i, column=column).value
            column_data.append(cell_value)
        return column_data

    # 获取某行所有值
    def get_row_value(self, row):
        columns = self.ws.max_column
        row_data = []
        for i in range(1, columns + 1):
            cell_value = self.ws.cell(row=row, column=i).value
            row_data.append(cell_value)
        return row_data

    def find_last_row(self):
        _row_sum, _ = self.get_row_col_sum()
        row_val = [None] * _row_sum
        while all(x is None for x in row_val):
            _row_sum -= 1
            row_val = self.get_row_value(_row_sum)

        return _row_sum


class Excel_writer:

    def __init__(self, _file_name):
        self.file = _file_name
        self.wb = Workbook()
        sheets = self.wb.sheetnames
        self.sheet = sheets[0]
        self.ws = self.wb[self.sheet]

    # 设置某个单元格的值
    def set_cell_value(self, row, column, cell_value):
        try:
            self.ws.cell(row=row, column=column).value = cell_value
            self.wb.save(self.file)
        except:
            self.ws.cell(row=row, column=column).value = "writefail"
            self.wb.save(self.file)



if __name__ == '__main__':
    sheet_idx = 0
    # path = 'D:\\MyData\\ex_pengzb\\Desktop\\testExcel\\'
    path = 'D:\\PycharmProjects\\demoProj\\cn\\excel\\'
    a_list = get_file_from_fold(_path=path)
    if len(a_list) == 0:
        print("err: 文件夹并没有.xls结尾的文件")
        os.abort()
    er = Excel_reader(_file_name=a_list[0], _sheet_idx=sheet_idx)
    row_sum, col_sum = er.get_row_col_sum()
    res_data_3 = er.get_row_value(3)
    real_row_sum = er.find_last_row()
    ic(real_row_sum)
    res_data_78 = er.get_row_value(row_sum - 5)
    res_data_79 = er.get_row_value(row_sum - 4)
    res_data_80 = er.get_row_value(row_sum - 3)
    ew = Excel_writer(r'D:\PycharmProjects\demoProj\cn\excel\output.xlsx')
    sheet_name = str(er.get_sheet())
    ew.set_cell_value(1, 1, sheet_name)
    for i in range(len(res_data_3)):
        ic(res_data_3[i])
        ew.set_cell_value(2, i + 1, res_data_3[i])
    for i in range(len(res_data_78)):
        ic(res_data_78[i])
        ew.set_cell_value(3, i + 1, res_data_78[i])
    for i in range(len(res_data_79)):
        ic(res_data_79[i])
        ew.set_cell_value(4, i + 1, res_data_79[i])
    for i in range(len(res_data_80)):
        ic(res_data_80[i])
        ew.set_cell_value(5, i + 1, res_data_80[i])
