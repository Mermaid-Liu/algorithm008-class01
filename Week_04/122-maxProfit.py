class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        lens=len(prices)
        for i in range(1,lens):
            j=prices[i]-prices[i-1]
            if j>0:
                profit+=j
        return profit
