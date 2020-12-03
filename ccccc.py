import pymysql

# 1.要链接数据库
host="129.204.62.26"
user="root"
password="1234"
port=3309
database="test"
conn=pymysql.connect(host=host,user=user,password=password,port=port,database=database)

# 2.创建一个游标
cur=conn.cursor()

# # 3.插入数据
# cur.execute("insert into test values(1,'tong')")
# cur.execute("commit")
# cur.close()

# # 查询数据
# cur.execute("select * from test")
# # 获取游标查询后的数据,取全部的数据，保存的类型是一个元祖
# data=cur.fetchall()
# print(data)
# cur.close()

# update操作，修改
# cur.execute("update test set id=3 where name='tong'")
# cur.execute("commit")
# cur.close()

# delete操作
# cur.execute("delete from test where id=3")
# cur.execute("commit")
# cur.close()
