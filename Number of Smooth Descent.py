class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        total = len(prices)
        x = 0

        for i in range(len(prices) - 1):
            if prices[i] - prices[i + 1] == 1:
                x += 1
                total += x
            else:
                x = 0

        return total
