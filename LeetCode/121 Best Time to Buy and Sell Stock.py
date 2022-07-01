class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        l, r = 0, 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                curr_profit = prices[r] - prices[l]
                max_profit = max(curr_profit, max_profit)
            r += 1
        return max_profit
