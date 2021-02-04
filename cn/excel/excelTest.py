import xlrd
import datetime
from datetime import date
import openpyxl
import re


# https://github.com/bozi0822/python_practice_m.git
# 比较两个list的差异
def get_diff(list1, list2):
    diff = [x for x in list1 if x not in list2]  # 在list1列表中而不在list2列表中
    if len(diff) == 0:
        diff = [x for x in list2 if x not in list1]  # 在list2列表中而不在list1列表中
    return diff


class Excel_reader:
    """excel读取类"""

    def __init__(self, _file_name, _sheet_idx):
        self.file_name = _file_name
        self.sheet_idx = _sheet_idx
        self.sheet = self.get_sheet()
        self.row_sum, self.col_sum = self.get_row_num_and_col_num()

    def get_sheet(self):
        """
        获取表
        :return:
        """
        # 打开文件
        wb = xlrd.open_workbook(filename=self.file_name)
        # 获取所有sheet的名字
        name = self.file_name
        str_list = name.split('\\')  # 截取生成表名
        print('文件名：' + str_list[len(str_list) - 1] + ':\n表名：', wb.sheet_names())
        # sheet1索引从0开始，得到sheet1表的句柄
        sheet = wb.sheet_by_index(self.sheet_idx)
        return sheet

    def get_row_num_and_col_num(self):
        """
        获取表的总列数和总行数
        :return:
        """
        # 行数
        row_num = self.sheet.nrows
        # 列数
        col_num = self.sheet.ncols
        print("行数row：" + str(row_num))
        print("列数col：" + str(col_num))
        return row_num, col_num

    def read_content(self, col_num):
        """
        读取表的内容
        :param col_num:
        :return:
        """
        _a_list = []
        _head_list = []
        for i in range(self.row_sum):
            row = self.sheet.row_values(i)
            # 表头不输出
            if i == 0:
                continue
            content = row[col_num]
            # print(content)
            _a_list.append(content)
        for j in range(self.col_sum):
            col = self.sheet.col_values(j)
            head = col[0]
            _head_list.append(head)

        return _a_list, _head_list

    def print_content(self):
        """
        打印表内容
        """
        for i in range(self.col_sum):
            print('=' * 150)
            _res_list, _head_list = self.read_content(col_num=i)
            print(_head_list[i], len(_res_list))
            print(_res_list)

    def create_table_sql(self):
        """
        获取表创建新表的脚本
        """
        res_list_0, head_list_0 = self.read_content(0)  # 获取到第1列数据
        res_list_1, _ = self.read_content(2)  # 获取到第3列数据
        table_name = self.get_table_name()
        sql = f"create table {table_name}(\n"
        for i in range(len(res_list_0)):
            sql += "   " + res_list_0[i] + " " + res_list_1[i]
            if i == (len(res_list_0) - 1):
                sql += "\n"
                continue
            sql += ",\n"
        print(sql + ");")

    def get_table_name(self):
        """
        获取表名
        """
        table_name = self.file_name.split("\\")[-1].split(".")[0]  # 截取文件名
        table_name = re.sub('[\u4e00-\u9fa5]', '', table_name)  # 去掉汉字
        table_name = str.upper(table_name)  # 大写
        return table_name


if __name__ == '__main__':
    sheet_idx = 0

    file_name5 = r'D:\MyData\ex_pengzb\Desktop\cr_punch_area字段.xls'
    er1 = Excel_reader(_file_name=file_name5, _sheet_idx=sheet_idx)
    er1.create_table_sql()

    file_name5 = r'D:\MyData\ex_pengzb\Desktop\equ_param_sandevice_list字段.xls'
    er2 = Excel_reader(_file_name=file_name5, _sheet_idx=sheet_idx)
    er2.create_table_sql()
