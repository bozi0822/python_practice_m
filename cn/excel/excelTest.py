import xlrd
import datetime
from datetime import date


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

    # def read_excel(self, file_name):
    #     # 打开文件
    #     wb = xlrd.open_workbook(filename=file_name)
    #     # 获取所有sheet的名字
    #     print(wb.sheet_names())
    #     sheet1 = wb.sheet_names()[0]
    #     # 获取第二个sheet的表明
    #     # sheet2 = wb.sheet_names()[1]
    #     # sheet1索引从0开始，得到sheet1表的句柄
    #     sheet1 = wb.sheet_by_index(0)
    #     rowNum = sheet1.nrows
    #     colNum = sheet1.ncols
    #     # s = sheet1.cell(1,0).value.encode('utf-8')
    #     s = sheet1.cell(1, 0).value
    #     print("行数：" + str(rowNum))
    #     print("列数：" + str(colNum))
    #     # 获取某一个位置的数据
    #     # 1 ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    #     # print(sheet1.cell(1, 2).ctype)
    #     # print(s)
    #     # print(s.decode('utf-8'))
    #     # 获取整行和整列的数据
    #     # 第二行数据
    #     row2 = sheet1.row_values(1)
    #     # 第二列数据
    #     cols2 = sheet1.col_values(2)
    #     print(row2[1])
    #     # print("\n")
    #     # python读取excel中单元格内容为日期的方式
    #     # 返回类型有5种
    #     # print(sheet1.row_values(28)[0])
    #     # num = '%d' % sheet1.row_values(28)[0]
    #     # print(num)
    #     # print(type(num))
    #     res_col1 = ''
    #     res_col2 = ''
    #     res_col3 = ''
    #     count = 0
    #     a_list = []
    #     for i in range(rowNum):
    #         row = sheet1.row_values(i)
    #         # print('row:' + str(row))
    #         # print(type(row[0]))
    #         # print(isinstance(row[0], float))
    #
    #         # content1 = row[0]
    #         # if isinstance(row[0], str):
    #         #     content1 = str(content1)
    #         # else:
    #         #     content1 = '%d' % content1
    #         # print("insert into SP_CATALOGUPDATE_YYZ(type_code,sp_name,sp_type,factory_name)values('"
    #         #       + content1 + "', '" + str(row[1]) + "', '" + str(row[2]) + "', '" + str(
    #         #     row[3]) + "');")
    #
    #         if i == 0:
    #             continue
    #         plan_code = row[0]
    #         res_col0 = '\'' + plan_code + '\''
    #         # plan_code = row[1]
    #         # res_col1 = '\'' + plan_code + '\''
    #         #
    #         # plan_code = row[2]
    #         # res_col2 = '\'' + plan_code + '\''
    #         #
    #         # plan_code = row[3]
    #         # res_col3 = '\'' + plan_code + '\''
    #
    #         count += 1
    #         a_list.append(plan_code)
    #         # print('update asset_card ac set ac.device_name = ' + res_col3 + ' where ac.device_code = ' + res_col1 + ';')
    #
    #     # print('res_col1 :')
    #     # print(res_col1)
    #     # print('res_col2 :')
    #     # print(res_col2)
    #     # print('res_col3 :')
    #     # print(res_col3)
    #     print('count => ' + str(count))
    #     print(a_list)
    #     return a_list


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

    file_name3 = r'D:\MyData\ex_pengzb\Downloads\EAM设备名称修改申请明细.xls'
    er3 = Excel_reader(file_name3, sheet_idx)
    # res_list1, head_list1 = er3.read_content(1)
    # res_list2, head_list2 = er3.read_content(2)
    # res_list3, head_list3 = er3.read_content(3)

    # print(res_list1)
    # print(head_list1[1], len(res_list1))
    # print(res_list2)
    # print(head_list1[2], len(res_list2))
    # print(res_list3)
    # print(head_list1[3], len(res_list3))

    for i in range(er3.col_sum):
        print('=' * 150)
        res_list, head_list = er3.read_content(col_num=i)
        print(head_list[i], len(res_list))
        print(res_list)
