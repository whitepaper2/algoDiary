#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/1/12 下午8:45
# @Author  : pengyuan.li
# @Site    : 
# @File    : 21.1_union_sets.py
# @Software: PyCharm

from collections import defaultdict


class UnionFindSets:
    def __init__(self, A):
        """
        维护父节点(字典)、高度(字典)、并查集个数
        :param A: 输入list
        """
        self.parent = {}
        self.rank = {}
        self.setsNum = len(A)
        self.sets = defaultdict(set)
        for a in A:
            self.parent[a] = a
            self.rank[a] = 1
            self.sets[a].add(a)

    def find(self, x):
        # while x != self.parent[x]:
        #     x = self.parent[x]
        # return self.parent[x]
        father = self.parent[x]
        if father != x:
            father = self.find(father)
        self.parent[x] = father
        return father

    def union(self, x, y):
        if not x or not y:
            return
        xHead = self.find(x)
        yHead = self.find(y)
        if xHead == yHead:
            return

        xRank = self.rank[xHead]
        yRank = self.rank[yHead]
        # if xRank >= yRank:
        #     self.parent[yHead] = xHead
        #     if xRank == yRank:
        #         self.rank[xRank] += 1
        # else:
        #     self.parent[xHead] = yHead
        if xRank < yRank:
            self.parent[xHead] = yHead
            self.sets[xHead].add(yHead)
        else:
            self.parent[yHead] = xHead
            self.sets[yHead].add(xHead)
            if xRank == yRank:
                self.rank[xHead] += 1
        self.setsNum -= 1

    def printSets(self, x):
        """
        打印x所在的集合元素
        :param x:
        :return:
        """
        print(self.sets[x])


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    ufs = UnionFindSets(nums)
    ufs.union(1, 3)
    print(ufs.parent, ufs.rank, ufs.setsNum)
    ufs.printSets(3)

    ufs.union(1, 3)
    print(ufs.parent, ufs.rank, ufs.setsNum)
    mydict = {'卡BIN国家与收货国家（非高风险）不一致且订单金额大于等于50': 17,
              '支付方式为信用卡': 84,
              '3DS_Challenge_特定国家和金额_更新': 18,
              'web设备状态异常_设备首次出现': 51,
              'IOS设备状态异常_设备首次出现': 4,
              '高风险国家': 309,
              'BR_高风险类目且3天内使用超过2张卡': 98,
              '高风险国家短时间内账户或设备使用多张信用卡': 73,
              'BR_30天内同一CPF关联卡号大于等于3': 50,
              '30天内有过被拒绝的交易': 109,
              '新用户且订单金额较大': 38,
              '邮箱模型_邮箱随机生成': 35,
              '模型分数规则': 45,
              'IOS越狱识别': 3,
              'GB站点新用户高风险类目且卡号复制黏贴': 76,
              '高风险国家用户短时间内使用多张信用卡（≥5张）': 28,
              'BR_30天内账户使用极多信用卡': 38,
              '短时间内多次尝试支付': 61,
              '测试_卡bin非US收货国家US': 3,
              '新用户订单金额大于等于500': 24,
              '安卓作弊工具识别': 62,
              '安卓设备状态异常_中风险': 24,
              '3DS_Challenge_高风险国家且高风险类目': 33,
              '新用户卡号全部复制黏贴且订单金额较大（信用卡数量≥2张）': 32,
              '非高风险国家30天内账户或设备关联信用卡数量较多（同一账户≥3张或同一设备ID≥5张）': 4,
              '非高风险国家10天内复制黏贴卡号数量过多（≥3张）': 2,
              '模型分数规则_10分': 39,
              '高风险国家10天内复制黏贴卡号数量过多（≥2张）': 60,
              '1天内设备交易次数过多（≥20次）': 34,
              '收货国家与账单国家不一致': 5,
              '历史人审结果为拒绝': 14,
              '测试_历史订单人工审核结果为拒绝': 14,
              '10天内卡号关联邮箱数量≥2且被审核或拒绝过': 1,
              '3DS_Challenge_高风险类目_AOA<30_AMT>99': 5,
              '安卓VPN代理识别': 10,
              '测试-相似地址标签': 14,
              '高风险国家新用户短时间内订单总额过高': 10,
              '测试_30天内账户关联信用卡数量极多': 4,
              '卡BIN国家与收货国家不一致且收货国家高风险': 5,
              '排除美国货代_卡BIN国家与收货国家（非高风险）不一致且订单金额大于等于50': 6,
              '新用户卡号复制黏贴且短时间内交易频率异常（信用卡数量≥2张）': 4,
              '1天内设备关联IP归属国家数过多（≥3个）': 2,
              '设备缺失': 2,
              'Ship=RU_SHIP<>BIN_Bin不等于UA/BY/KZ_COPY_AOA<7': 2,
              'IP归属国家≠卡bin国家≠收货国家': 2,
              '历史订单支付失败原因包含盗卡或黑名单': 2,
              'BR/MX_30天内电话号码关联账户数大于2': 5,
              '安卓模拟器识别': 1,
              'web设备状态异常_隐身模式': 2,
              '非高风险国家短时间内账户或设备使用多张信用卡（≥3张）': 1}
    xx = sorted(mydict.items(), key=lambda x: -x[-1])
    print(xx)
    import pandas as pd

    rules = [('模型分数规则', 0.056),
     ('30天内有过被拒绝的交易', 0.054),
     ('GB站点新用户高风险类目且卡号复制黏贴', 0.051),
     ('3DS_Challenge_高风险类目_AOA<7_AMT>149', 0.044),
     ('卡BIN国家与收货国家（非高风险）不一致且订单金额大于等于50', 0.04),
     ('高风险国家短时间内账户或设备使用多张信用卡', 0.039),
     ('非高风险国家30天内账户或设备关联信用卡数量较多（同一账户≥3张或同一设备ID≥5张）', 0.038),
     ('卡BIN国家与收货国家不一致且收货国家非高风险', 0.036),
     ('卡BIN国家与收货国家不一致且收货国家高风险', 0.036),
     ('非高风险国家短时间内账户或设备使用多张信用卡（≥3张）', 0.036),
     ('高风险国家10天内复制黏贴卡号数量过多（≥2张）', 0.034),
     ('短时间内多次尝试支付', 0.033),
     ('30天内账户或设备使用卡BIN国家数量过多（≥3个）', 0.031),
     ('BR_高风险类目且3天内使用超过2张卡', 0.029),
     ('新用户订单金额大于等于500', 0.029),
     ('3天内账户使用卡bin国家数量过多（≥3个）', 0.025),
     ('测试_30天内账户关联信用卡数量极多', 0.025),
     ('新用户卡号全部复制黏贴且订单金额较大（信用卡数量≥2张）', 0.024),
     ('非高风险国家新用户短时间内使用多张信用卡（≥5张）', 0.024),
     ('高风险国家用户短时间内使用多张信用卡（≥5张）', 0.023),
     ('非高风险国家10天内复制黏贴卡号数量过多（≥3张）', 0.021),
     ('安卓作弊工具识别', 0.02),
     ('BR_30天内同一CPF关联卡号大于等于3', 0.019),
     ('安卓VPN代理识别', 0.019),
     ('收货国家与账单国家不一致', 0.019),
     ('IOSVPN代理识别', 0.016),
     ('BR_30天内账户使用极多信用卡', 0.014),
     ('IP归属国家≠卡bin国家≠收货国家', 0.014),
     ('历史人审结果为拒绝', 0.013),
     ('US货代地址欺诈', 0.011),
     ('web设备状态异常_中风险', 0.011),
     ('web设备状态异常_隐身模式', 0.011),
     ('1天内设备交易次数过多（≥20次）', 0.01),
     ('历史订单支付失败原因包含盗卡或黑名单', 0.01),
     ('排除美国货代_卡BIN国家与收货国家（非高风险）不一致且订单金额大于等于50', 0.007),
     ('设备获取异常_高风险', 0.007),
     ('测试_卡bin非US收货国家US', 0.006),
     ('IOS越狱识别', 0.005),
     ('安卓ROOT识别', 0.005),
     ('新用户Florida州疑似货代欺诈', 0.005),
     ('来源IP归属国家与真实IP归属国家不匹配', 0.005),
     ('Ship=RU_SHIP<>BIN_Bin不等于UA/BY/KZ_COPY_AOA<7', 0.004),
     ('卡binUS特定高风险国家新用户', 0.004),
     ('银行卡号命中历史拒付卡号黑名单_观察', 0.004),
     ('30天内手机号码关联邮箱数量大于等于2', 0.003),
     ('BR_新用户卡bin不等于BR', 0.003),
     ('IOShttp代理识别', 0.003),
     ('法国海外省份规则', 0.003),
     ('测试_卡bin国家与收货国家为US且IP不等于US', 0.003),
     ('IOS设备状态异常_高风险', 0.002),
     ('命中客户自定义黑名单', 0.002),
     ('安卓设备状态异常_中风险', 0.002),
     ('3DS_Challenge_高风险类目_Ship=FR/PL/ES_COPY_AOA<7', 0.001),
     ('IP归属国家高风险且不等于卡BIN国家', 0.001),
     ('SHIP=US_BIN<>SHIP_单个SKU数量≧2_copy_AOA≦7', 0.001),
     ('安卓http代理识别', 0.001),
     ('排除法国海外省_卡BIN国家与收货国家不一致且订单金额大于等于50', 0.001),
     ('邮箱模型_临时邮箱', 0.001),
     ('非高风险国家新用户短时间内订单总额过高', 0.001),
     ('高风险国家新用户短时间内订单总额过高', 0.001)]
    print(len(rules))
