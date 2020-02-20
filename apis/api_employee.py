
"""
    功能：主要实现跟员工管理相关的接口
"""
from apis.base import Base


class ApiEmployee(Base):


    #新增员工
    def post_emp(self,mobile,username,work_number,**kwargs):
        post_emp_data = {"mobile":mobile,"username":username,"workNumber":work_number}
        if kwargs:
            post_emp_data.update(kwargs)
        return self.post(self.get_url('/api/sys/user'),data=post_emp_data)

    #查询员工
    def get_emp(self,emp_id):
        return self.get(self.get_url('/api/sys/user',emp_id))


    #删除员工
    def delete_emp(self,emp_id):
        return self.delete(self.get_url('/api/sys/user',emp_id))


if __name__ == '__main__':
    api = ApiEmployee()
    #res = api.post_emp("13810201020","test001","1000")
    res1 = api.delete_emp('1229953808112898048')
    print(res1)