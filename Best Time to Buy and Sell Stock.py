#Best Time to Buy and Sell Stock
#问题描述
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#一次股票交易得到的最大利润
#不要在循环中使用min max

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
        minP=max(prices)
        maxP=min(prices)
        minI=maxP
        profit=0
        for p in prices:
            if p<minP:
                minP=p
                maxP=minI
            if p>maxP:
                maxP=p
            if maxP-minP>profit:
                profit=maxP-minP
        return profit

a= Solution()
print a.maxProfit2([100,99,98,97,96,95,94])