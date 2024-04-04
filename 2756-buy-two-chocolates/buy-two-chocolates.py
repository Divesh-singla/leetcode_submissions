class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
    ### first approach
        # result = 0
        # prices.sort()
        # if prices[0]<money:

        #     result+=prices[0]
        #     result+=prices[1]
        #     if (money-result)>=0:
        #         return money-result
        #     else:
        #         return money
        # else:
        #     return money

    ### second approach 
        prices.sort()

        if prices[0] + prices[1] > money:
            return money
        else:
            return money - (prices[0] + prices[1])

        