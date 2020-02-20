
"""
    功能:主要实现的是对新增员工接口进行测试
"""
import time
import pytest,logging
from mysql.mysql_employee import get_employee_data
from apis.api_employee import ApiEmployee
from datas.data_employee import DataEmployee


emp_data = DataEmployee()

class TestThreePararmPostEmployee():


    def setup_class(self):

        self.emp_object = ApiEmployee()
        emp_id = get_employee_data(emp_data.mobile)[0]
        if emp_id:
            self.emp_object.delete_emp(emp_id)

        self.res = self.emp_object.post_emp(emp_data.mobile,emp_data.username,emp_data.work_number)
        self.db_data = get_employee_data(emp_data.mobile)
        logging.info("数据库查询数据:{}".format(self.db_data))

    @pytest.mark.P0
    def test_code(self):
        assert 10000 == self.res.get('code')


    #断言mobile，username，work_number
    @pytest.mark.P1
    def test_three_bt(self):
        assert emp_data.mobile == self.db_data[1]
        assert emp_data.username == self.db_data[2]
        assert emp_data.work_number == self.db_data[3]


    #断言非必填字段为null
    @pytest.mark.P2
    def test_kx_params(self):
        # assert self.db_data[4] is None
        # assert self.db_data[5] is None
        # assert self.db_data[6] is None
        # assert self.db_data[7] is None
        # assert self.db_data[8] is None
        for dt in self.db_data[4:]:
            assert dt is None


class TestAllPararmPostEmployee():


    def setup_class(self):
        self.emp_object = ApiEmployee()
        emp_id = get_employee_data(emp_data.mobile)[0]
        if emp_id:
            self.emp_object.delete_emp(emp_id)

        self.res = self.emp_object.post_emp(emp_data.mobile,emp_data.username,emp_data.work_number,**emp_data.emp_add_kx)
        self.db_data = get_employee_data(emp_data.mobile)
        logging.info("数据库查询数据:{}".format(self.db_data))

    @pytest.mark.P0
    def test_code(self):
        assert 10000 == self.res.get('code')


    #断言八个字段的数据
    @pytest.mark.P1
    def test_all_field(self):
        assert emp_data.mobile == self.db_data[1]
        assert emp_data.username == self.db_data[2]
        assert emp_data.work_number == self.db_data[3]
        assert emp_data.emp_add_kx.get('timeOfEntry') == self.db_data[4].strftime("%Y-%m-%d")
        assert emp_data.emp_add_kx['formOfEmployment'] == self.db_data[5]
        assert emp_data.emp_add_kx['departmentId'] == self.db_data[6]
        assert emp_data.emp_add_kx['departmentName'] == self.db_data[7]
        assert emp_data.emp_add_kx['correctionTime'] == self.db_data[8].strftime("%Y-%m-%d")
