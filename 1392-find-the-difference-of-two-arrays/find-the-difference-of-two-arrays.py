class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = [[],[]]

        # if len(nums1) == len(nums2):
        #     for x in range(len(nums1)):
        #         if nums1[x] not in nums2:
        #             result[0].append(nums1[x])
        #         if nums2[x] not in nums1:
        #             result[1].append(nums2[x])
        # else:
        for y in nums1:
            if y not in nums2:
                result[0].append(y)
        for z in nums2:
            if z not in nums1:
                result[1].append(z)

        return result