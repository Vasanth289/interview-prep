"""
You are given an array of stock prices for a day. Each element in the array represents the stock price at a given time.
The time difference between each element is 1 second. You can buy and sell the stock only once.
There should a time gap of atleast 5 seconds between buying and selling the stock.
You need to find the maximum profit you can make by buying and selling the stock at the right time.
"""

def max_profit(prices):
    maxProf = 0
    minSoFar = prices[0]

    for i in range(len(prices)):
        if i < len(prices) - 5:
            minSoFar = min(minSoFar, prices[i])

        if i >= 5:
            maxProf = max(maxProf, prices[i] - minSoFar)

    return maxProf

if __name__ == "__main__":
    # Test cases
    prices = [7, 1, 5, 9, 6, 4, 8]
    print(max_profit(prices))  # Output: 5 (Buy at 1 and sell at 6)
    
    prices = [7, 6, 4, 3, 1]
    print(max_profit(prices))  # Output: 0 (No transaction is done)
    
    prices = [1, 2, 3, 4, 5, 6]
    print(max_profit(prices))  # Output: 4 (Buy at 1 and sell at 5)

    prices = [60, 60, 60, 3, 2, 3, 20, 40, 5, 40, 3, 2, 0, 0, 60]
    print(max_profit(prices))  # Output: 58 (Buy at 2 and sell at 60)