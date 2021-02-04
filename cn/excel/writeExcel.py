#!/usr/bin/python
# coding=utf-8
# ==============================================================================
#
#       Filename:  demo.py
#    Description:  excel operate
#        Created:  Tue Apr 25 17:10:33 CST 2017
#         Author:  Yur
#
# ==============================================================================

import xlwt

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('My Worksheet')

# 写入excel
# 参数对应 行, 列, 值
worksheet.write(0, 0, label='this is test')

# 保存
workbook.save('Excel_test.xls')
