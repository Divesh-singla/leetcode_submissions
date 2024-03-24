class Solution:
    def isPalindrome(self, s: str) -> bool:
        finalStr = ""
        for x in s.lower():
            if ord(x) in range(97,123) or ord(x) in range(48,58) :
                finalStr+=x


        # print(finalStr)
        return(finalStr == finalStr[::-1])
