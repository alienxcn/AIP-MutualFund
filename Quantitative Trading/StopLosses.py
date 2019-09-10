def initialize(context):
    run_daily(period, time = "every_bar")
    g.security = '000001.XSHE'

def period(context):
    order(g.security, 100)
    cost = context.portfolio.positions['000001.XSHE'].avg_cost
    price = context.portfolio.positions['000001.XSHE'].price
    
    ret = price/cost - 1

    print('成本价: %s' % cost)
    print('现价: %s' % price)
    print('收益率: %s' % ret)

    if ret < -0.01:
        order_target('000001.XSHE', 0)
        print('触发止损')