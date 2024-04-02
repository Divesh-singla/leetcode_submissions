class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
    # # BRUTE FORCE APPROACH
        result = 0
        for x in range(len(nums)):
            for y in range(x):
                if nums[x] == nums[y]:
                    result+=1
        return result

    # # APPROACH 2

        