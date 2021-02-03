import xlrd
import datetime
from datetime import date
import openpyxl
import re


# https://github.com/bozi0822/python_practice_m.git
def get_diff(list1, list2):
    diff = [x for x in list1 if x not in list2]  # 在list1列表中而不在list2列表中
    if len(diff) == 0:
        diff = [x for x in list2 if x not in list1]  # 在list2列表中而不在list1列表中
    return diff

class Excel_reader:

    def __init__(self, _file_name, _sheet_idx):
        self.file_name = _file_name
        self.sheet_idx = _sheet_idx
        self.sheet = self.get_sheet()
        self.row_sum, self.col_sum = self.get_row_num_and_col_num()

    def get_sheet(self):
        # 打开文件
        wb = xlrd.open_workbook(filename=self.file_name)
        # 获取所有sheet的名字
        name = self.file_name
        str_list = name.split('\\')
        print('文件名：' + str_list[len(str_list) - 1] + ':\n表名：', wb.sheet_names())
        # sheet1索引从0开始，得到sheet1表的句柄
        sheet = wb.sheet_by_index(self.sheet_idx)
        return sheet

    def get_row_num_and_col_num(self):
        # 行数
        row_num = self.sheet.nrows
        # 列数
        col_num = self.sheet.ncols
        print("行数row：" + str(row_num))
        print("列数col：" + str(col_num))
        return row_num, col_num

    def read_content(self, col_num):
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
        for i in range(self.col_sum):
            print('=' * 150)
            _res_list, _head_list = self.read_content(col_num=i)
            print(_head_list[i], len(_res_list))
            print(_res_list)

    def create_table_sql(self):
        res_list_0, head_list_0 = self.read_content(0)
        res_list_1, _ = self.read_content(2)
        table_name = self.file_name.split("\\")[-1].split(".")[0]  # 截取文件名
        table_name = re.sub('[\u4e00-\u9fa5]', '', table_name)  # 去掉汉字
        table_name = str.upper(table_name)  # 大写
        sql = f"create table {table_name}(\n"
        for i in range(len(res_list_0)):
            sql += "   " + res_list_0[i] + " " + res_list_1[i]
            if i == (len(res_list_0) - 1):
                sql += "\n"
                continue
            sql += ",\n"
        print(sql + ");")


if __name__ == '__main__':
    file_name1 = r'D:\MyData\ex_pengzb\Desktop\pm_plan_det字段.xls'
    file_name2 = r'D:\MyData\ex_pengzb\Desktop\pm_plan_det_his_new字段.xls'
    sheet_idx = 0
    # er1 = Excel_reader(file_name1, sheet_idx)
    # res_list1 = er1.read_content(0)
    # print('========================================================================================================')
    # er2 = Excel_reader(file_name2, sheet_idx)
    # res_list2 = er2.read_content(0)
    # print('========================================================================================================')
    # print('res_list1=>', res_list1)
    # print('res_list2=>', res_list2)
    #
    # c = get_diff(res_list1, res_list2)
    # print('diff => ', c)

    # file_name3 = r'D:\MyData\ex_pengzb\Downloads\EAM设备名称修改申请明细.xls'
    # er3 = Excel_reader(file_name3, sheet_idx)
    # res_list1, head_list1 = er3.read_content(1)
    # res_list2, head_list2 = er3.read_content(2)
    # res_list3, head_list3 = er3.read_content(3)

    # print(res_list1)
    # print(head_list1[1], len(res_list1))
    # print(res_list2)
    # print(head_list1[2], len(res_list2))
    # print(res_list3)
    # print(head_list1[3], len(res_list3))

    # for i in range(er3.col_sum):
    #     print('=' * 150)
    #     res_list, head_list = er3.read_content(col_num=i)
    #     print(head_list[i], len(res_list))
    #     print(res_list)

    # file_name4 = r'D:\MyData\ex_pengzb\Desktop\DEVICE_PARAMETER_REALTIME字段.xls'
    # er = Excel_reader(file_name4, sheet_idx)
    # res_list_0, head_list_0 = er.read_content(0)
    # res_list_1, _ = er.read_content(2)
    # er.print_content()
    # sql = "create table DEVICE_PARAMETER_REALTIME(\n"
    # for i in range(len(res_list_0)):
    #     sql += "   " + res_list_0[i] + " " + res_list_1[i] + ",\n"
    # print(sql + ");")

    file_name5 = r'D:\MyData\ex_pengzb\Desktop\cr_punch_area字段.xls'
    er1 = Excel_reader(_file_name=file_name5, _sheet_idx=sheet_idx)
    er1.create_table_sql()

    file_name5 = r'D:\MyData\ex_pengzb\Desktop\equ_param_sandevice_list字段.xls'
    er2 = Excel_reader(_file_name=file_name5, _sheet_idx=sheet_idx)
    er2.create_table_sql()
