class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        result = 0
        
        # while (nums)!=[]:
        #     if len(nums)>1:
        #         result+=int(f'{nums[0]}{nums[-1]}')
        #         del nums[0]
        #         del nums[-1]

        #     else:
        #         result+=nums[0]
        #         del nums[0]
        # return result

## approach 2
        i = 0
        j = len(nums)-1
        result = 0

        while i<=j:
            if i==j:
                result+=nums[i]
                break
            result+=int(f'{nums[i]}{nums[j]}')
            i+=1
            j-=1
        return result

