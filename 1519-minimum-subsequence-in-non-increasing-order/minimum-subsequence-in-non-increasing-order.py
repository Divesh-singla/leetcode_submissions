class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        for x in range(1,len(nums)+1):
            if sum(nums[:x])>sum(nums[x:]):
                return nums[:x]
# class Solution:
#     def minSubsequence(self, nums: List[int]) -> List[int]:
#         nums.sort(reverse=True)
#         total_sum = sum(nums)
#         subsequence_sum = 0
#         subsequence = []

#         for num in nums:
#             subsequence_sum += num
#             subsequence.append(num)
#             if subsequence_sum > (total_sum - subsequence_sum):
#                 return subsequence