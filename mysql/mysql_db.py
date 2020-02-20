
# === 连接数据库的基本流程
#导包
#创建连接对象
#创建游标
#执行sQL
#关闭游标
#关闭连接
import pymysql
from setting import DbConfig

class Mysql():

    def __init__(self):
        self.conn = pymysql.connect(**DbConfig.de_config)

    #查询所有数据
    def get_all(self,sql):
        # sql = 'select id,mobile,username,work_number,time_of_entry,form_of_employment,department_id,department_name,correction_time from bs_user where mobile = "{}"'.format(
        #         #     mobile)
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()
        finally:
            self.conn.close()

if __name__ == '__main__':
    sql = 'select id,mobile,username,correction_time from bs_user where mobile = "13800000002"'
    mysql = Mysql()
    res = mysql.get_all(sql)
    print(res)
