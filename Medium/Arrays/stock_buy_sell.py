from typing import List
def max_profit_bruteforce(prices: List[int]) -> int:
    """
    Brute-force approach to maximize profit by choosing the best days to buy and sell stock.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """    
    n = len(prices)
    max_profit = float("-inf")
    for i in range(n):
        for j in range(i+1, n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit, profit)
    return max_profit 

def max_profit_optimal(prices: List[int]) -> int:
    """
    Optimal approach to maximize profit by iterating through the prices array only once.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """    
    n = len(prices)
    min_price = float("inf")
    max_profit = float("-inf")
    for price in prices:
        min_price = min(price, min_price)
        profit = price - min_price
        max_profit = max(profit, max_profit)
    return max_profit

prices = [7,1,5,3,6,4]
print("Brute-force Approach:", max_profit_bruteforce(prices))
print("Optimal Approach:", max_profit_optimal(prices))