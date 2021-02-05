import time

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
        if not (filename.__contains__('.xls') or filename.__contains__('.xlsx')) or (filename.__contains__('output')):
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
        time.sleep(1)
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

    # 寻找最后一行
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


def banner_paint():
    print("""
     ______     __  __     ______     ______     __            ______   ______     ______     __        
    /\  ___\   /\_\_\_\   /\  ___\   /\  ___\   /\ \          /\__  _\ /\  __ \   /\  __ \   /\ \       
    \ \  __\   \/_/\_\/_  \ \ \____  \ \  __\   \ \ \____     \/_/\ \/ \ \ \/\ \  \ \ \/\ \  \ \ \____  
     \ \_____\   /\_\/\_\  \ \_____\  \ \_____\  \ \_____\       \ \_\  \ \_____\  \ \_____\  \ \_____\ 
      \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_____/        \/_/   \/_____/   \/_____/   \/_____/                                                                                              
    """)


input_fold_name = ''


def init():
    banner_paint()
    global input_fold_name
    input_fold_name = input("请输入需要汇总文件夹的路径：")
    input_fold_name += '\\'
    print("开始提取...")
    time.sleep(2)


if __name__ == '__main__':
    # init()
    sheet_idx = 0
    # D:\PycharmProjects\demoProj\cn\excel\
    input_fold_name = 'D:\\MyData\\ex_pengzb\\Desktop\\testExcel\\'
    # input_fold_name = 'D:\\PycharmProjects\\demoProj\\cn\\excel\\'
    print("获取输入的文件夹的excel文件...")
    a_list = get_file_from_fold(_path=input_fold_name)
    if len(a_list) == 0:
        print("err: 文件夹并没有.xls结尾的文件")
        os.abort()
    ic(a_list)
    time.sleep(1)
    print("导入excel完成！需要合并的文件有", len(a_list), "个")
    time.sleep(2)
    row_counter = 0
    ew = Excel_writer(f'{input_fold_name}\output.xlsx')  # 新建output文件
    for i in range(len(a_list)):
        er = Excel_reader(_file_name=a_list[i], _sheet_idx=sheet_idx)
        row_sum, col_sum = er.get_row_col_sum()
        res_data_3 = er.get_row_value(3)
        real_row_sum = er.find_last_row()
        ic(real_row_sum)
        last_row_2 = er.get_row_value(real_row_sum - 2)
        last_row_1 = er.get_row_value(real_row_sum - 1)
        last_row = er.get_row_value(real_row_sum)
        sheet_name = str(er.get_sheet())
        row_counter += 1
        ew.set_cell_value(row_counter, 1, sheet_name)
        row_counter += 1
        for j in range(len(res_data_3)):
            ic(res_data_3[j])
            ew.set_cell_value(row_counter, j + 1, res_data_3[j])
        row_counter += 1
        for j in range(len(last_row_2)):
            ic(last_row_2[j])
            ew.set_cell_value(row_counter, j + 1, last_row_2[j])
        row_counter += 1
        for j in range(len(last_row_1)):
            ic(last_row_1[j])
            ew.set_cell_value(row_counter, j + 1, last_row_1[j])
        row_counter += 1
        for j in range(len(last_row)):
            ic(last_row[j])
            ew.set_cell_value(row_counter, j + 1, last_row[j])

