# 获取一个股票最近5个交易日最高价的平均价。

w = attribute_history('300462.XSHE', 5, fields='high')
avghcost = mean(w.values)
print(avghcost)

# 生成一个list，其中为上证指数成分股中流通市值最大的5个股票的股票代码。

stock = get_index_stocks('000001.XSHG')
q = query(valuation.code, valuation.market_cap).filter(valuation.code.in_(stock)).order_by(valuation.market_cap.desc()).limit(5)
gp = get_fundamentals(q)
## get_fundamentals函数的返回值是一个pandas.DataFrame类型。
print(gp)
print(gp.iloc[:,[0]])