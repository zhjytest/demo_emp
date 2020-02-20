

#查询新增员工后的数据，通过mobile查询
from mysql.mysql_db import Mysql
import logging

def get_employee_data(mobile):
    res = None
    sql = 'select id,mobile,username,work_number,time_of_entry,form_of_employment,department_id,' \
          'department_name,correction_time from bs_user where mobile = "{}"'.format(
        mobile)
    m = Mysql()
    print("=="*20)
    get_result = m.get_all(sql)
    if get_result:
        res = get_result[0]
    logging.info("查询数据:{}".format(res))
    return res
