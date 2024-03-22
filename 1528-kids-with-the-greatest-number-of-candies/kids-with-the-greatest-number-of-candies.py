class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxx = max(candies)
        for x in range(len(candies)):
            inter = candies[x] + extraCandies
            result.append(inter >= maxx)
        return result