import cx_Oracle

conn = cx_Oracle.connect('oraeam/eam(2014@10.16.20.123:1523/eamtst1')
cur = conn.cursor()  # 创建游标
sql = "select h.* from run_fault_reg h where h.apply_code = 'GZ1712260002'"
cur.execute(sql)  # 执行sql语句
rows = cur.fetchall()  # 获取数据 #也可以使用fetchmany(100),fetchone()

tup = rows[0]
res = {}
print(type(rows[0]))
list1 = []
list2 = []

for i in cur.description:
    # print(i[0])
    list1.append(i[0])
    # print(type(i[0]))

for j in tup:
    # print(j)
    list2.append(j)
    # print(type(j))

res_dict = dict(zip(list1, list2))
print(res_dict['DEPT_ID'])
cur.close()
conn.close()  # 关闭数据库连接
