class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        result = 0
        prices.sort()
        if prices[0]<money:

            result+=prices[0]
            result+=prices[1]
            if (money-result)>=0:
                return money-result
            else:
                return money
        else:
            return money

        