# 找出市值排名最小的前stocksnum只股票作为要买入的股票
# 如果已经持有的股票的市值已经不够小而不在要买入的股票中，则卖出这些股票。
# 买入股票，买入金额为可用资金的stocksnum分之一。

def initialize(context):
    run_daily(period, time='every_bar')
    g.stocksnum = 10

def period(context):
    # 找出市值排名最小的前stocksnum只股票作为要买入的股票
    scu = get_index_stocks('000001.XSHG') + get_index_stocks('399106.XSHE')
    q = query(valuation.code
                ).filter(
                    valuation.code.in_(scu)
                ).order_by(
                    valuation.circulating_market_cap.asc()
                ).limit(g.stocksnum)
    df = get_fundamentals(q)
    buylist = list(df['code'])
    
    # 如果已经持有的股票的市值已经不够小而不在要买入的股票中，则卖出这些股票。
    for stock in context.portfolio.positions:
        if stock not in buylist:
            order_target(stock, 0)
    
    # 买入股票，买入金额为可用资金的stocksnum分之一。
    position_per_stk = context.portfolio.cash / g.stocksnum
    for stock in buylist:
        order_value(stock, position_per_stk)


import pandas as pd
file = 'D:\example.xls'
df = pd.DataFrame(pd.read_excel(file))
print df