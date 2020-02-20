from pprint import pprint


def cut(num,c):
    c=10**(-c)
    return (num//c)*c


def equal_installments_of_principal_and_interest(money,years_rate,num,period=None):
    """
        等额本息计算公式
        :parameter
            money : 贷款本金
            years_rate : 年利率
            num : 还款总期数
            period : 第几期，不输入会把全部期都输出
        :return
            每月还款总额，利息，本金
        :说明
            等额本息计算公式：
            月利率 = 年利率 / 12
            每月还款本息 = 贷款金额 * 月利率 *  (1 + 月利率) ** 还款月数 / ( 1 + 月利率) ** 还款月数 -1
            每月还款利息： 贷款金额 * 月利率 * ((1 + 月利率) ** 还款月数 - (1+月利率) **(还款月序号-1)) /(1+月利率) ** 还款月数 -1
        :举例
            equal_installments_of_principal_and_interest(12000,0.16,12)     //本金12000，年利率16%，借款期限12期计算所有数据
            equal_installments_of_principal_and_interest(12000,0.16,12，2)  //只计算第二期
    """
    dt = dict()
    if years_rate > 1 or years_rate <=0:
        return '输入的年利率不正确，需要是小于1且大于0的数'
    if not isinstance(num,int):
        return '还款的总期数必须为整数'
    if num <= 0:
        return '还款的总期数必须为大于0的整数'

    month_rate = years_rate/12
    value = (1 + month_rate) ** num

    if period is None:
        period =num
    if period < 1:
        return '还款期数不能小于1!'
    if period >num:
        return '还款期数不能大于总期数!'
    for x in range(1,period+1):
        temp = (1 + month_rate) ** (x-1)
        amount_due = float(('%.2f' % (money * month_rate * value / ( value - 1))))     #应还金额
        repayment_interest = float(('%.2f'% (money * month_rate * (value - temp) / (value -1)))) #每月还款利息
        principal = float(('%.2f' % (amount_due - repayment_interest)))  #每月还款本金
        lst = []
        if period in [num,x]:
            lst.append("第{}期应还本息:{}".format(x,amount_due))
            lst.append("第{}期应还利息:{}".format(x,repayment_interest))
            lst.append("第{}期应还本金:{}".format(x,principal))
            dt[x] = lst
    return dt


def pay_interest_and_interest_at_the_end_of_the_day(money,year_rate,days):
    """
        按天计息到期还本息计算公式：
        :parameter
            money:借款金额
            year_rate:年利率
            days:借款天数
        :return
            利息
        举例：pay_interest_and_interest_at_the_end_of_the_day(1000,0.12,30)

    """
    if year_rate < 0 or year_rate > 1:
        return '年利率必须是在0~1的数'
    if isinstance(money,str):
        return '借款金额必须是浮点数或整数'
    if not isinstance(days,int):
        return '借款天数必须是整数'
    return float('%.2f' % (money * year_rate * days / 360))


def pay_interest_and_interest_at_the_end_of_the_month(money,year_rate,month):
    """
        到期还本还息，按月付息的计算公式：
        :parameter
            money:借款金额
            year_rate:年利率
            days:借款天数
        :return
            利息
        举例：pay_interest_and_interest_at_the_end_of_the_month(1000,0.12,30)

    """
    if year_rate < 0 or year_rate > 1:
        return '年利率必须是在0~1的数'
    if isinstance(money,str):
        return '借款金额必须是浮点数或整数'
    if not isinstance(month,int):
        return '借款天数必须是整数'
    return float('%.2f' % (money * year_rate * month / 12))


if __name__ == '__main__':
    #pprint(equal_installments_of_principal_and_interest(12000,0.16,12,2))
    print(pay_interest_and_interest_at_the_end_of_the_day(3000,0.11,33))
