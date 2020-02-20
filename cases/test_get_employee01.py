import logging
import pytest
from apis.api_employee import ApiEmployee
from datas.data_employee import DataEmployee
from mysql.mysql_employee import get_employee_data

emp_data = DataEmployee().emp_search

@pytest.fixture(scope="class")
def get_data():
    emp_object = ApiEmployee()
    #通过手机号查询员工数据
    emp_db_data = get_employee_data(emp_data.get('mobile'))
    #如果数据库中有员工数据，进行删除
    if emp_db_data:
        emp_id = emp_db_data[0]
        emp_object.delete_emp(emp_id)
    # 不管如何都会进行调用添加员工接口
    res = emp_object.post_emp(emp_data.get('mobile'), emp_data.get('username'), emp_data.get('work_number'))
    # 获取员工id
    get_emp_id = res.get('data').get('id')
    result = emp_object.get_emp(get_emp_id)
    return result






class TestGetEmployee():



    @pytest.mark.P0
    def test_code(self,get_data):
        assert 10000 == get_data.get('code')

    @pytest.mark.P1
    def test_qt_field(self,get_data):
        assert emp_data.get('mobile') == get_data.get('data').get('mobile')
        assert emp_data.get('username') == get_data.get('data').get('username')
        assert emp_data.get('work_number') == get_data.get('data').get('workNumber')



