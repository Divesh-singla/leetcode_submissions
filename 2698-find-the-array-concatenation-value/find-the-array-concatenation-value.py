class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        
        while (nums)!=[]:
            if len(nums)>1:
                result+=int(f'{nums[0]}{nums[-1]}')
                del nums[0]
                del nums[-1]

            else:
                result+=nums[0]
                del nums[0]
        return result
