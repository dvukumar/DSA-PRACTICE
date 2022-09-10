class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        prev = prices[0]
        total_profit = 0
        
        for curr in prices:
            profit = curr - prev
            if profit>0:
                total_profit+=profit
            prev = curr
        
        return total_profit