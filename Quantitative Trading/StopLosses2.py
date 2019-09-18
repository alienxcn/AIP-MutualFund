def initialize(context):
	run_daily(period, time='every_bar')
	g.security = ['000001.XSHE', '000002.XSHE']

def period(context):
	for stk in g.security:
		order(stk, 100)

		cost = context.portfolio.positions[stk].avg_cost
		price = context.portfolio.positions[stk].price

		ret = price/cost - 1
		if ret<-0.03:
			order_target(stk, 0)
			print('触发止损')