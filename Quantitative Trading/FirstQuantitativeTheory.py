def initialize(context):
    run_daily(period, time='every_bar')
    g.security = '000001.XSHE'

def period(context):
    order(g.security, 100)