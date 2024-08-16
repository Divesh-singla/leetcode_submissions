class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        result = []
        part = None

        for x in range(len(nums)):
            inter = target-nums[x]
            if inter in nums[:x]:
                part = 1
                result.append(x)
            elif inter in nums[x+1:]:
                part = 2
                result.append(x)
        if part==1:
            for y in range(len(nums[:result[0]])):
                if target-result[0]==nums[y]:
                    result.append(y)
                    break
        elif part==2:
            for y in range(len(nums[result[0]+1:])):
                if target-result[0]==nums[y]:
                    result.append(y)
                    break


        return result

        

        # result = []
        
        # for x in range(len(nums)):
        #     for y in range(x):
        #         if target == nums[x]+nums[y]:
        #             result.append(x)
        #             result.append(y)
        #             break
        # return result
            

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         result = []
#         counter = 0
#         iterator = 1
#         status = True

#         while status:

#             if counter != iterator:
#                 if nums[counter]+nums[iterator] == target:
#                     result.append(counter)
#                     result.append(iterator)

#             if iterator == len(nums)-1:
#                 counter+=1
#                 iterator = counter

#             if counter == len(nums)-1:
#                 status = False

#             iterator+=1

#         return (result)