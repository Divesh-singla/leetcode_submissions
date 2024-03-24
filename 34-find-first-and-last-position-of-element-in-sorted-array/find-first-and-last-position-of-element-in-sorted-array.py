class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = []
        for x in range(len(nums)):
            if nums[x] == target:
                result.append(x)
        if result == []:
            return [-1,-1]
        else:
            return [min(result),max(result)]