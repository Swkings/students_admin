import pymysql
import sys
sys.path.append(r'D:\Swk\CodeSpace\Python\tedu\07.12\3-UI版学员管理系统')

conn = pymysql.connect("localhost", "root", "wk0917", "tedu")

cursor = conn.cursor()

# cursor.execute("SELECT * FROM students")
#
# data = cursor.fetchone()
#
# print(data)
#
# conn.close()
