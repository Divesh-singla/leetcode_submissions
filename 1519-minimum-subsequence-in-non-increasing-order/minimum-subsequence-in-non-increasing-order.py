class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        subArray = []
        subResult=0
        numsSum = sum(nums)
        for x in nums:
            subArray.append(x)
            subResult+=x
            if subResult>(numsSum-subResult):
                return subArray