## 量化交易

量化交易是指借助现代统计学和数学的方法，利用计算机技术来进行交易的证券投资方式。

1. 从一个灵感开始。
2. 把灵感细化成明确的可执行的交易策略。
3. 把策略转成程序。
4. 检验策略效果。（回测和模拟交易）
5. 进行实盘交易并不断维护修正。

## 常用的下单函数

1. order(security, amount)，购买一定数量的股票。
2. order_target(security, amount), 通过买卖，将股票的仓位调整到一定数量。
3. order_value(security, value)，买卖一定价值量的股票。
4. order_target_value(security, value)，通过买卖，将股票仓位调整至一定价值量。