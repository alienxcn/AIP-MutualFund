# -*- coding:UTF-8 -*-
# 获取基金的历史单位净值与累积净值数据，并打印出折线图

import requests
import time
import execjs
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def getUrl(fscode):
  head = 'http://fund.eastmoney.com/pingzhongdata/'
  tail = '.js?v='+ time.strftime("%Y%m%d%H%M%S",time.localtime())
  return head+fscode+tail

def getWorth(fscode):
    # 用requests获取到对应的文件
    content = requests.get(getUrl(fscode))
    # 使用execjs获取到相应的数据
    jsContent = execjs.compile(content.text)
    # 基金名称、代码、单位净值、累计净值、原费率、现费率、最小申购金额、基金持仓股票代码、基金持仓债券代码
    fS_name = jsContent.eval('fS_name')
    fS_code = jsContent.eval('fS_code')
    netWorthTrend = jsContent.eval('Data_netWorthTrend')
    ACWorthTrend = jsContent.eval('Data_ACWorthTrend')
    fund_sourceRate = jsContent.eval('fund_sourceRate')
    fund_Rate = jsContent.eval('fund_Rate')
    fund_minsg = jsContent.eval('fund_minsg')
    stockCodes = jsContent.eval('stockCodes')
    zqCodes = jsContent.eval('zqCodes')
    # 收益率
    syl_1n = jsContent.eval('syl_1n')
    syl_6y = jsContent.eval('syl_6y')
    syl_3y = jsContent.eval('syl_3y')
    syl_1y = jsContent.eval('syl_1y')
    # 提取出里面的净值
    netWorth = []
    ACWorth = []
    for dayWorth in netWorthTrend[::-1]:
        netWorth.append(dayWorth['y'])
    for dayACWorth in ACWorthTrend[::-1]:
        ACWorth.append(dayACWorth[1])
    # 提取时间对应单位净值
    netWorth_withTime = {}
    for dayWorth in netWorthTrend[::-1]:
        netWorth_withTime[time.strftime('%Y-%m-%d',time.localtime(int(dayWorth['x'])/1000))] = dayWorth['y']
    

    print(fS_name,fS_code)
    return netWorth, ACWorth, netWorth_withTime

def drawPlt(netWorth_withTime):
    plt.figure(figsize=(20,5))
    x = list(netWorth_withTime.keys())[:500][::-1]
    y = list(netWorth_withTime.values())[:500][::-1]
    plt.plot(y)
    plt.show()

netWorth, ACWorth, netWorth_withTime = getWorth('163407')


days = 131
money_each_pay = 10
money_totally = 0
mutual_fund_value = 0
mutual_fund_number = 0
sorted(netWorth_withTime, reverse = True)
for key, value in netWorth_withTime.items():
    days = days - 1
    money_totally = money_totally + money_each_pay
    mutual_fund_number = mutual_fund_number + money_each_pay/value
    if days == 0:
        print('自%s开始定投，每次定投金额%d元\n' % (key,money_each_pay))
        break
    
mutual_fund_value = mutual_fund_number * netWorth_withTime['2019-09-06']

print('投入本金:%d' % money_totally)
print('基金价值:%f' % mutual_fund_value)
print('利润率:%f%%' % ((mutual_fund_value/money_totally - 1.0) * 100))

    