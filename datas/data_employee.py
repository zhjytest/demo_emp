import random


class DataEmployee():

    mobile = "13810201024"
    username = "test001"
    work_number = "2000"

    emp_add_kx = {
        "timeOfEntry": "2019-07-01",
        "formOfEmployment": 1,
        "departmentId": "1066240656856453120",
        "departmentName": "Test",
        "correctionTime": "2019-11-30"
    }

    emp_search = {
        "mobile": "13900957522",
        "username": "name998356",
        "work_number": "21205023",
        "timeOfEntry": "2019-10-06",
        "formOfEmployment": 1,
        "departmentId": "1066238836272664576",
        "departmentName": "财务部",
        "correctionTime": "2019-12-05"
    }


    def generator_mobile(self,num=None):

        qz_list = ["138",'139','130','133']
        mobile = None
        if num:
            for x in range(num):
                #print(x)
                mob = random.choice(qz_list)
                hm = random.randint(10000000, 99999999)
                mobile = mob + str(hm)
                print(mobile)
        else:
            mob = random.choice(qz_list)
            hm = random.randint(10000000, 99999999)
            mobile = mob + str(hm)
        #print(mob)

        return mobile


if __name__ == '__main__':
    dt = DataEmployee()
    mobile = dt.generator_mobile(10)
    print(mobile)