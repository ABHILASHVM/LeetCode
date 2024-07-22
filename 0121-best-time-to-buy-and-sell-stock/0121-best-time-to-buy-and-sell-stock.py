class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maxi=0
        # for i in range(len(prices)-1):
        #     if (max(prices[i+1:])-prices[i]) > maxi:
        #         maxi=max(prices[i+1:])-prices[i]
        # return maxi
        

        buy_price = prices[0]
        profit = 0

        for p in prices[1:]:
            if buy_price > p:
                buy_price = p
            
            profit = max(profit, p - buy_price)
        
        return profit