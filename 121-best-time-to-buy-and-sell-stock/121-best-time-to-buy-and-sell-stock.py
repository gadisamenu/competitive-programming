class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b_price = prices[0]
        max_profit= 0
        for price in prices:
            if price < b_price: b_price = price
            
            max_profit= max(max_profit,price-b_price)
            
        return max_profit
