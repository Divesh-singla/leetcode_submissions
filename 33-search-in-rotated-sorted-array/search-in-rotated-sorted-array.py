class Solution:
    def search(self, nums: List[int], target: int) -> int:
        result = -1
        for x in range(len(nums)):
            if nums[x] == target:
                result = x
                break
        return result