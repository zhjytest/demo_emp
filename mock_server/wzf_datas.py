order_payApply_data = {
    '成功': {
        "platSignFlow": "P112001180724191525000074",
        "supportOrgName": "宝付",
        "platOrderNo": 'null',
        "platFlowNo": "10001180724190516000024",
        "mobileNo": "15810553242",
        "status": "1",
        "resCode": "C301100000000",
        "opType": "1",
        "resMsg": "成功",
        "codeLockStatus": "1",
        "sign": "fb359a58f2f7621bb71d8f3d26c0c70e"
    },
    '操作失败': {
        "platSignFlow": "null",
        "supportOrgName": 'null',
        "platOrderNo": 'null',
        "platFlowNo": 'null',
        "mobileNo": 'null',
        "status": "2",
        "resCode": "E201100000132",
        "opType": "6",
        "resMsg": "当前操作失败，请您稍后再试",
        "codeLockStatus": "0",
        "sign": "4b69d823d5b358030c8d4e9340a9aad6"
    },
    '0002': {"resCode": "C301100000001", "resMsg": "失败"}

}

order_payConfirm_data = {
    '支付成功': {
        "platFlowNo": "10001180724190516000024",
        "resCode": "C301100000000",
        "opType": "1",
        "resMsg": "成功",
        "codeLockStatus": "1",
        "sign": "bcffd6163aed1241b30e40fa09270762"
    },
    '验证码错误': {
        "platFlowNo": "10001180724190516000024",
        "resCode": "E301105100021",
        "opType": "1",
        "resMsg": "您输入的验证码有误，请重新输入",
        "codeLockStatus": "1",
        "sign": "7ec4ee83f213d9df64a1c6cad7d84691"
    }
}

payInfo_get_data = {
    '成功': {
        "payWayChoice": "MER",
        "payWayList": [{
            "sort": "null",
            "itemCode": "1",
            "itemName": "银行卡快捷支付（富友）"
        }],
        "mermberInfo": {
            "certType": "00",
            "isRealNameCertify": "01",
            "realName": "5jcg/ciEXmA=",
            "certNo": "hTvNZFYGgE610/ke7kEhObu1/jPZU3Yt",
            "platUserId": "1201805031502260011"
        },
        "fuiouAccount": {
            "cardNo": "oPmM0fOPzpLjvKgVJF1PrwDJLDFv48xH",
            "phoneNo": "1JM1fnV3I1pHGdJ3t9WzWA==",
            "bankNo": "CMB",
            "isAuth": "1",
            "bankName": "招商银行",
            "fuYouAcc": "15810553242",
            "payAmtLimit": {
                "dayLimit": 10000.0000,
                "singleLimit": 10000.0000,
                "paySuccessAmt": "null",
                "daySuccLimit": 0,
                "daySuccCountLimit": 0,
                "dayFailLimit": 0,
                "dayFailCountLimit": 99999999,
                "daySuccLimitBal": 0,
                "daySuccCountLimitBal": 0,
                "dayFailLimitBal": 0,
                "dayFailCountLimitBal": 0,
                "monthSuccCountLimit": 0,
                "monthFailLimit": 0,
                "monthFailCountLimit": 99999999,
                "monthFailCountLimitBal": 0,
                "monthFailLimitBal": 0,
                "monthSuccCountLimitBal": 0,
                "monthSuccLimitBal": 0,
                "monthSuccLimit": 0,
                "mothLimit": 99999999.0000,
                "balDayAmt": "null",
                "yearLimit": "null"
            },
            "name": "5jcg/ciEXmA=",
            "status": "01"
        },
        "currentOpenInfo": {
            "showContent": 2,
            "openStatus": 0,
            "content": "null",
            "status": 0
        },
        "currentAccount": "null",
        "resCode": "C301100000000",
        "opType": "1",
        "resMsg": "成功",
        "codeLockStatus": "1",
        "sign": "8b3051534585d15c4845d7aa59dffb48"
    },
}


member_openAccount_data = {
    "绑卡成功":{"resMsg":"绑卡成功，返回的正确数据格式需要提供给管理员"},
    "校验卡信息失败": {
        "fuYouAcc": 'null',
        "openFlow": 'null',
        "status": "03",
        "resCode": "E201100000132",
        "opType": "6",
        "resMsg": "当前操作失败，请您稍后再试",
        "codeLockStatus": "0",
        "sign": "4153e35525f669e9ea499a923d890eba"
    }
}


member_query_data = {
    "查询成功": {
        "cardNo": 'null',
        "phoneNo": 'null',
        "bankNo": 'null',
        "dayLimit": 'null',
        "singleLimit": 'null',
        "isAuth": 'null',
        "bankName": 'null',
        "fuYouAcc": 'null',
        "monthlimit": 'null',
        "name": 'null',
        "status": "04",
        "resCode": "C301100000000",
        "opType": "1",
        "resMsg": "成功",
        "codeLockStatus": "1",
        "sign": "dce1d610bdab1154527d71aafce11247"
    },
    "查询失败": {
        "cardNo": 'null',
        "phoneNo": 'null',
        "bankNo": 'null',
        "dayLimit": 'null',
        "singleLimit": 'null',
        "isAuth": 'null',
        "bankName": 'null',
        "fuYouAcc": 'null',
        "monthlimit": 'null',
        "name": 'null',
        "status": "04",
        "resCode": "C301100000001",
        "opType": "1",
        "resMsg": "失败",
        "codeLockStatus": "1",
        "sign": "dce1d610bdab1154527d71aafce11247"
    }
}


card_limitamtlist_data = {
    "限额列表": {
        "qlrmList": [{
            "bankNo": "CITIC",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中信银行",
            "monthlimit": 99999999.0000,
            "bankLog": "14"
        }, {
            "bankNo": "BOC",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国银行",
            "monthlimit": 99999999.0000,
            "bankLog": "3"
        }, {
            "bankNo": "BCM",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "交通银行",
            "monthlimit": 99999999.0000,
            "bankLog": "15"
        }, {
            "bankNo": "CEB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国光大银行",
            "monthlimit": 99999999.0000,
            "bankLog": "11"
        }, {
            "bankNo": "CIB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "兴业银行",
            "monthlimit": 99999999.0000,
            "bankLog": "13"
        }, {
            "bankNo": "ABC",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国农业银行",
            "monthlimit": 99999999.0000,
            "bankLog": "2"
        }, {
            "bankNo": "HXB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "华夏银行",
            "monthlimit": 99999999.0000,
            "bankLog": "7"
        }, {
            "bankNo": "ICBC",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国工商银行",
            "monthlimit": 99999999.0000,
            "bankLog": "1"
        }, {
            "bankNo": "PAB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "平安银行",
            "monthlimit": 99999999.0000,
            "bankLog": "10"
        }, {
            "bankNo": "CGB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "广发银行",
            "monthlimit": 99999999.0000,
            "bankLog": "9"
        }, {
            "bankNo": "CCB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国建设银行",
            "monthlimit": 99999999.0000,
            "bankLog": "4"
        }, {
            "bankNo": "CMB",
            "dayLimit": 99999999.0000,
            "singleLimit": 100000.0000,
            "bankName": "招商银行",
            "monthlimit": 99999999.0000,
            "bankLog": "12"
        }, {
            "bankNo": "CMBC",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国民生银行",
            "monthlimit": 99999999.0000,
            "bankLog": "8"
        }, {
            "bankNo": "SPDB",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "上海浦东发展银行",
            "monthlimit": 99999999.0000,
            "bankLog": "5"
        }, {
            "bankNo": "PSBC",
            "dayLimit": 99999999.0000,
            "singleLimit": 4000.0000,
            "bankName": "中国邮政储蓄银行",
            "monthlimit": 99999999.0000,
            "bankLog": "6"
        }],
        "resCode": "C301100000000",
        "opType": "1",
        "resMsg": "成功",
        "codeLockStatus": "1",
        "sign": "8b3051534585d15c4845d7aa59dffb48"
    }
}


service_check_data = {
    "成功": {
        "resCode": "C301100000000",
        "opType": "1",
        "resMsg": "成功",
        "codeLockStatus": "1",
        "sign": "8b3051534585d15c4845d7aa59dffb48"
    }
}