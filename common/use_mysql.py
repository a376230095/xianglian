import pymysql

from common.get_config import cf
from common.get_log import log


class Mysql:

    # 初始化链接mysql数据库
    def __init__(self):
        try:
            # log.info("开始链接数据库")
            host = cf.get_value("mysql", "host")
            user = cf.get_value("mysql", "user")
            password = cf.get_value("mysql", "password")
            port = int(cf.get_value("mysql", "port"))
            database = cf.get_value("mysql", "database")
            # log.info(f"链接的数据库为：{host}，{user}，{password},{port},{database}")
            self.conn = pymysql.connect(host=host, user=user, password=password, port=port, database=database)
        except Exception as e:
            log.info(f"数据库链接失败，原因是{e}")

    # 定义select语句
    def select(self,query):
        # 新建游标
        cur=self.conn.cursor()
        log.info(f"现在在执行select语句：{query}")
        # 执行select语句
        try:
            cur.execute(query)
            # 获取数据
            data=cur.fetchall()
            log.info("select语句执行成功")
            return data
        except Exception as e:
            log.info(f"select语句执行失败，原因：{e}")
        finally:
            cur.close()


    # 定义delete语句
    def delete(self,query):
        # 新建游标
        cur=self.conn.cursor()
        log.info(f"现在在执行delete语句：{query}")
        try:
            # 执行delete语句
            cur.execute(query)
            # delete数据成功，肯定要commit
            cur.execute("commit")
            log.info("delete语句执行成功")
        except Exception as e:
            # delete失败了，数据是不是要回滚
            cur.execute("rollback")
            log.info(f"delete语句执行失败，原因：{e}")
        finally:
            cur.close()

    # 定义insert语句
    def insert(self,query):
        # 新建游标
        cur=self.conn.cursor()
        log.info(f"现在在执行insert语句：{query}")
        try:
            # 执行insert语句
            cur.execute(query)
            cur.execute("commit")
            log.info("insert语句执行成功")
        except Exception as e:
            # delete失败了，数据是不是要回滚
            cur.execute("rollback")
            log.info(f"insert语句执行失败，原因：{e}")
        finally:
            cur.close()

        # 定义update语句
    def update(self,query):
        # 新建游标
        cur=self.conn.cursor()
        log.info(f"现在在执行update语句：{query}")
        try:
            # 执行update语句
            cur.execute(query)
            cur.execute("commit")
            log.info("update语句执行成功")
        except Exception as e:
            # update失败了，数据是不是要回滚
            cur.execute("rollback")
            log.info(f"update语句执行失败，原因：{e}")
        finally:
            cur.close()

mysql=Mysql()


if __name__ == "__main__":
    a=Mysql()
    # a.insert("insert into test values(1,'haha')")
    # b=a.select("select * from test")
    # print(b)
    # a.update("update test set id=10 where name='haha'")
    a.delete("delete from test where id=10")