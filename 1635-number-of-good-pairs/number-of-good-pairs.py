class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    # # BRUTE FORCE APPROACH
        # result = 0
        # for x in range(len(nums)):
        #     for y in range(x):
        #         if nums[x] == nums[y]:
        #             result+=1
        # return result

    # # APPROACH 2
        setNums = set(nums)
        result = 0

        for x in (setNums):
            count = nums.count(x)
            if count>=2:
                for y in range(1,count):
                    result+=(count-y)
        return result


        