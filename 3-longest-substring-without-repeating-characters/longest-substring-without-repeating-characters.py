class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        result = 0
        charSet = set()

        for r in range(len(s)):

            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1

            charSet.add(s[r])
            result = max(result,r-l+1)
        return result




        # i = 0 
        # j = 0
        # status = True
        # string = ""
        # result = []
        # output = 0
        # print(len(arr))
        # if len(s)>0:
        #     while status:
                
                
        #         if s[j] not in string:
        #             string+=s[j]
                    
        #         else:
        #             if string not in result:
        #                 result.append(string)
        #             string = s[j]
                    
        #         j+=1
                        
        #         if j==len(s)-1:
                    
        #             if s[j] not in string:
        #                 string+=s[j]
        #                 if string not in result:
        #                     result.append(string)

        #             else:
        #                 result.append(string)
        #             i+=1
        #             j=i
        #             string=""
                    
        #         if i==len(s)-1:
        #             status = False
        #             if string not in result and string!="":
        #                 result.append(string)
        


        # for x in result:
        #     if len(x)>output:
        #         output = len(x)
        # return output