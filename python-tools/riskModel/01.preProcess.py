# !/usr/bin/env python
# -*- coding: utf-8 -*-
import pandas as pd

# dc数据分析
dfp = pd.read_csv('./rawdata_up/tdl_aopeng_20210301_20210909.csv', sep='\00')
# 删除异常行
dfp = dfp.drop_duplicates(subset=["transId"], keep="last")
dfp = dfp[~dfp['logisticsFee'].isin(['111'])]
dfp = dfp[dfp["accountEmail"] != "wuyingli0521@163.com"]
dfp = dfp[~dfp['accountName'].isin(["testtest", "aaaa", "ffff", "ssss", "aaff", "aabb", "吧j",
                                    "ffffffffffff", "ssff", "cccccc", "bbbbbbb", "sssss"])]

mydict = {'orderNo': '业务订单号',
          'transId': '交易流水号',
          'eventOccurTime': '事件发生时间',
          'accountName': '客户姓名',
          'phoneCodeNumber': '手机国际区号数字',
          'phoneCode': '手机国际区号',
          'accountMobile': '手机号码',
          'accountAge': '账户年龄',
          'accountEmail': '用户电子邮箱',
          'registerTime': '账户注册时间',
          'merchandiseName': '商品名称',
          'category1': '商品一级类目',
          'oderItemCount': '订单商品数量',
          'skuNumber': 'SKU编码',
          'skuCountMax': '单个SKU数量最大值',
          'billingPhoneNumber': '账单电话',
          'billingCity': '账单城市',
          'billingCountry': '账单国家',
          'billingState': '账单州',
          'billingZipCode': '账单地址邮编',
          'billingAddress': '账单地址',
          'billingEmail': '账单邮箱',
          'shippingEmail': '收货邮箱',
          'shippingCountry': '收货国家',
          'shippingAddress': '收货地址',
          'shippingState': '收货州',
          'shippingCity': '收货城市',
          'shippingZipCode': '收货地址邮编',
          'payTotalAmount': '订单总金额',
          'payAmount': '交易金额',
          'logisticsFee': '物流费用金额',
          'cardType': '卡类型',
          'isInstallment': '是否分期',
          'installmentCount': '分期数',
          'currencyType': '交易币种',
          'cardBin': '卡BIN',
          'isoa2': '卡bin国家英文简码',
          'deviceType': '设备端',
          'orderMode': '订单模式',
          'deviceId': '设备ID',
          'paymentMethod': '支付方式',
          'cardNumber': '银行卡号',
          'cardBrand': '卡组织名称',
          'cardCategory': '信用卡类别',
          'isCardNumberCopy': '卡号是否复制黏贴',
          'paymentResult': '支付结果',
          'isCardScan': '是否使用扫卡功能',
          'ipAddress': '来源IP',
          'ip2': 'IP前两段',
          'ip3': 'IP3',
          'ipAddressCountryCode': 'IP地区码',
          'ipAddressCountry': 'IP归属地国家',
          'ipProvince': 'IP归属地省份',
          'ipAddressCity': 'IP归属地城市',
          'trueipaddresscountrycode': '真实IP归属地简码',
          'trueipaddressprovince': '真实IP归属地省份',
          'trueipaddresscity': '真实IP归属地城市',
          'errorReason': '支付失败原因',
          'logisticsType': '物流类型',
          'isCouponUsed': '是否使用COUPON',
          'isLogisticsInsurance': '是否使用物流保险',
          'chargebackReason': '拒付原因',
          'finalDecision': '风控决策结果',
          'chargebackReason2': '拒付原因2'}

dfp.rename(columns=mydict, inplace=True)


def func_(a, b, c, d):
    if a in ['Other Fraud - Card Absent Environment', 'No Cardholder Authorization'] \
            or b in ['Other Fraud - Card Absent Environment', 'No Cardholder Authorization'] \
            or d == "Reject":
        return 1
    elif c == 'fail':
        return -1
    else:
        return 0


dfp['label'] = dfp.apply(lambda x: func_(x.拒付原因, x.拒付原因2, x.支付结果, x.风控决策结果), axis=1)
dfp.to_csv("./features/dfp_features1.csv", index=None)
