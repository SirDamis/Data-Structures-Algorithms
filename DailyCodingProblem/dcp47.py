"""
Daily Coding Problem - Day 47

Given an array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock
once. You must buy before you can sell.

Example: Input: [9, 11, 8, 5, 7, 10] Output: 5
"""
def maxStockProfit(arr):
    max_profit = 0
    n = len(arr)
    l, r = 0, 1
    while r < n:
        if arr[r] > arr[l]:
            curr_profit = arr[r] - arr[l]
            max_profit = max(max_profit, curr_profit)
            r += 1
        else:
            l = r
            r += 1

    return max_profit

arr = [7, 6, 1, 0]
print(maxStockProfit(arr))
