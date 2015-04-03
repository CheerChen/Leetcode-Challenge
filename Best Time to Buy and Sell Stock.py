#Best Time to Buy and Sell Stock
#问题描述
#If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#一次股票交易得到的最大利润
#多次股票交易得到的最大利润
#不要在循环中使用min max
#注意峰值的判断

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

    def maxProfit2(self, prices):
        if len(prices)<2:
            return 0
        minP=prices[0]
        maxP=prices[0]
        profit=0
        i=0
        l=len(prices)
        for p in prices:
            if p>maxP:
                maxP=p
            if p<minP:
                minP=p
            # top element and hold untill price down
            if i+1<l and maxP==p and prices[i+1]<p:
                profit+=(p-minP)
                minP=p
                maxP=prices[i+1]
            #last element if we can make one more deal
            if i+1==l and minP<prices[-1]:
                profit+=prices[-1]-minP
            i+=1
        return profit

a= Solution()
print a.maxProfit([100,99,98,97,96,95,94])
print a.maxProfit2([5,2,3,2,6,6,2,9,1,0,7,4,5,0])