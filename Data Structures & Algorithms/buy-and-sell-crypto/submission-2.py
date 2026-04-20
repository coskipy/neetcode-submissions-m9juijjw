class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        buy_day = 0
        max_profit = 0

        for day in range(len(prices)):
            price = prices[day]

            if price < buy:
                buy = min(buy, price)
                buy_day = day

            if day > buy_day:
                max_profit = max(max_profit, price - buy)

        return max_profit