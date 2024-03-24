class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pointer1 = 0
        pointer2 = 1

        while pointer1<=pointer2 and pointer2<len(nums):

            if nums[pointer1] == nums[pointer2]:
                pointer2 += 1
            else:
                nums[pointer1+1] = nums[pointer2]
                pointer1 += 1
        return pointer1+1
        
        