import time

from cn.excel.sqlGenerator import ExcelOp
from icecream import ic

topic = '数据修正'
update = '【操作】'
insert = '【备份】'
check = '【检查单据是否存在】'

updateName = topic + update + 'update' + time.strftime("%Y%m%d-%H%M%S", time.localtime())
insertName = topic + insert + 'insert' + time.strftime("%Y%m%d-%H%M%S", time.localtime())
countName = topic + check + 'count' + time.strftime("%Y%m%d-%H%M%S", time.localtime())

chg_type = '\'修改\''
chg_desc = '\'部分自主维护实施单，专业点检实施单和专业润滑实施单的实际完工时间有误，因此申请数据修正实际完工时间\''

def pm_plan_update():
    path = r'D:\PycharmProjects\demoProj\cn\excel\test.xlsx'
    excel_op = ExcelOp(file=path, sheet_no=0)
    exe_code = excel_op.get_col_value(1)
    # ic(exe_code)
    end_date = excel_op.get_col_value(2)
    # ic(end_date)
    update1 = excel_op.get_col_value(6)
    # ic(update1[0])
    update2 = excel_op.get_col_value(7)
    # ic(update2[0])
    update3 = excel_op.get_col_value(8)
    # ic(update3[0])
    update4 = excel_op.get_col_value(9)
    # ic(update4[0])

    for i in range(len(exe_code)):
        if i < 3 or (str(end_date[i]) == 'None' and str(exe_code[i]) == 'None'):
            continue
        updateSql = str(update1[i]) + str(end_date[i]) + str(update2[i]) + str(end_date[i]) + str(update3[i]) + str(exe_code[i]) + str(update4[i]) + '\n'
        with open('D:\\PycharmProjects\\demoProj\\cn\\excel\\' + updateName + '.sql', 'a+') as a:
            a.write(updateSql)

    left = excel_op.get_col_value(10)
    # ic(left[0])
    right = excel_op.get_col_value(11)
    # ic(right[0])
    exe_code_str = ''
    for i in range(len(exe_code)):
        if i < 3 or (str(end_date[i]) == 'None' and str(exe_code[i]) == 'None'):
            continue
        exe_code_str += str(left[i]) + str(exe_code[i]) + str(right[i]) + '\n'

    exe_code_str = exe_code_str[0:len(exe_code_str) - 2]

    insertSql = "insert into geam.pm_plan_his \n" \
                "  select sysdate as chg_date,\n" \
                "         '彭镇波' as chg_user_name,\n" \
                "         " + chg_type + " as chg_type,\n" \
                "         " + chg_desc + " as chg_desc,\n" \
                "         pp.* \n" \
                "    from geam.pm_plan pp \n" \
                "   where pp.exe_code in (" + exe_code_str + ");"
    with open('D:\\PycharmProjects\\demoProj\\cn\\excel\\' + insertName + '.sql', 'a+') as a:
        a.write(insertSql)

    countSql = "select count(1) from geam.pm_plan pp where pp.exe_code in (" + exe_code_str +");"
    with open('D:\\PycharmProjects\\demoProj\\cn\\excel\\' + countName + '.sql', 'a+') as a:
        a.write(countSql)

if __name__ == '__main__':
    pm_plan_update()
