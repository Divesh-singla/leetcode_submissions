class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        result = max(nums)
        for x in range(len(nums)):
            if nums[x] == result:
                return x