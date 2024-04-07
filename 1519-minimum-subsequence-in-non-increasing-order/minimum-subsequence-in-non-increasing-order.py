class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        for x in range(1,len(nums)+1):
            if sum(nums[:x])>sum(nums[x:]):
                return nums[:x]
