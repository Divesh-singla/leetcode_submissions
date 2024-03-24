class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        pointer1 = 0
        pointer2 = 1
        result = 0
        while pointer2<len(prices):
            inter = prices[pointer2]-prices[pointer1]
            
            if prices[pointer1] < prices[pointer2]:
                result = max(inter,result)
            else:
                pointer1 = pointer2
            pointer2+=1
  
        return result



        