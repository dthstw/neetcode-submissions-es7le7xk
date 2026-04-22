class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        b = 0

        for i in range(1, len(prices)):
            if prices[b] > prices[i]:
                b = i
            else:
                maxProfit = max(maxProfit, prices[i] - prices[b])

        return maxProfit
            
# [5,1,5,6,7,1,10]
# 7: b = 0, i = 1 prices[b] = 5, prices[1] = 1 -> b = i = 1 
# 5: b = 1, i = 2 prices[b] = 1 prices[i] = 5 profit = 4 -> maxProfit = 4
# 3: b = 1, i = 3 prices[b] = 1 prices[i] = 3 prodit = 2 -> maxProfit = 4
# b = 1, i = 
# 