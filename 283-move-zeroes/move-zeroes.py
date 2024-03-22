class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # result = []
        # count = 0
        # for x in nums:
        #     if x == 0:
        #         count+=1
        #     else:
        #         result.append(x)
        # nums[:] = result + [0]*count
        

        #### _____________________________________two pointer approach______________________________________
        i = 0
        j = 1
        if 0 in nums:
            while j <len(nums):

                if nums[i] == 0:
                    nums[i],nums[j] = nums[j],nums[i]
                    j+=1
                
                else:
                    i+=1

                if j < i:
                    j = i+1

        """
        Do not return anything, modify nums in-place instead.
        """