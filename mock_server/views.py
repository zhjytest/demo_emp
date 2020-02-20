#coding:utf-8


from flask import jsonify
from flask import request
from app.datas.wzf_datas import *
from app.datas.err_datas import err_datas
from app.utils.dt import match_rule
from . import wzf





@wzf.route('/gateway/order/payConfirm',methods=['GET','POST'])
def pay_confirm():
    """微支付-支付接口"""
    dt00 = order_payConfirm_data['支付成功']
    dt01 = order_payConfirm_data['验证码错误']

    dict_data = request.values
    platFlowNo = dict_data.get('platFlowNo')
    if platFlowNo != None:
        dt00['platFlowNo'] = platFlowNo
        dt01['platFlowNo'] = platFlowNo

    if match_rule(dict_data,'0000'):
        return jsonify(dt00)
    if match_rule(dict_data,'0001'):
        return jsonify(dt01)
    return jsonify(err_datas['未定义错误'])


@wzf.route('/payInfo/get',methods=['GET','POST'])
def pay_info_get():
    """微支付-支付结果查询接口"""
    dict_data = request.values
    if match_rule(dict_data,'0000'):
        return jsonify(payInfo_get_data['成功'])
    return jsonify(err_datas['未定义错误'])


@wzf.route('/gateway/member/openAccount',methods=['GET','POST'])
def open_account():
    """微支付-绑卡开户接口"""
    dict_data = request.values

    if match_rule(dict_data,'0000'):
        return jsonify(member_openAccount_data['绑卡成功'])
    if match_rule(dict_data,'0001'):
        return jsonify(member_openAccount_data['校验卡信息失败'])
    if match_rule(dict_data,'0000',dict_data):
        return jsonify(member_openAccount_data['校验卡信息失败'])
    return jsonify(err_datas['未定义错误'])



@wzf.route('/gateway/member/query',methods=['GET','POST'])
def member_query():
    """微支付-账户查询接口"""
    dict_data = request.values

    if match_rule(dict_data,'0000'):
        return jsonify(member_query_data['查询成功'])
    if match_rule(dict_data,'0001',dict_data):  #传入参数为空时，返回失败
        return jsonify(member_query_data['查询失败'])
    if match_rule(dict_data,'0001'):
        return jsonify(member_query_data['查询失败'])
    return jsonify(err_datas['未定义错误'])



@wzf.route('/gateway/card/limitamtlist',methods=['GET','POST'])
def limit_amt_list():
    """微支付-限额列表"""
    dict_data = request.values
    if match_rule(dict_data,"0000"):
        return jsonify(card_limitamtlist_data['限额列表'])
    return jsonify(err_datas['未定义错误'])



@wzf.route('/service/check',methods=['GET','POST'])
def service_check():
    """微支付-服务检查"""
    dict_data = request.values
    if match_rule(dict_data,"0000"):
        return jsonify(service_check_data['成功'])
    return jsonify(err_datas['未定义错误'])







