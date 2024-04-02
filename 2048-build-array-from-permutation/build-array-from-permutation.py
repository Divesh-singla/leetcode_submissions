class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        if nums!=[]:
            for x in range(len(nums)):
                ans.append(nums[nums[x]])
            return ans
        else:
            return []