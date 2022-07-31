class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy = prices[0]
        max_profit = 0
        for i in range(1,len(prices)):
            curr = prices[i]
            if curr<buy:
                buy = curr
            else:
                profit = curr-buy
                max_profit = max(max_profit,profit)
        print(max_profit)
        return max_profit