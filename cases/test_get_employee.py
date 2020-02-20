import logging
import pytest
from apis.api_employee import ApiEmployee
from datas.data_employee import DataEmployee
from mysql.mysql_employee import get_employee_data

emp_data = DataEmployee().emp_search

class TestGetEmployee():

    def setup_class(self):
        self.emp_object = ApiEmployee()
        emp_id = get_employee_data(emp_data.get('mobile'))[0]
        self.res = self.emp_object.get_emp(emp_id)
        logging.info("查询接口的数据:{}".format(self.res))


    @pytest.mark.P0
    def test_code(self):
        assert 10000 == self.res.get('code')

    @pytest.mark.P1
    def test_qt_field(self):
        assert emp_data.get('mobile') == self.res.get('data').get('mobile')
        assert emp_data.get('username') == self.res.get('data').get('username')
        assert emp_data.get('work_number') == self.res.get('data').get('workNumber')
        assert emp_data.get('timeOfEntry') in self.res.get('data').get('timeOfEntry')
        assert emp_data.get('formOfEmployment') == self.res.get('data').get('formOfEmployment')
        assert emp_data.get('departmentId') == self.res.get('data').get('departmentId')
        assert emp_data.get('departmentName') == self.res.get('data').get('departmentName')
        assert emp_data.get('correctionTime') in self.res.get('data').get('correctionTime')



