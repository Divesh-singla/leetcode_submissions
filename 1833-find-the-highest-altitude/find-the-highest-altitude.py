class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        inter = 0
        for x in (gain):
            inter+=x
            result = max(result,inter)
        return result
