class Solution:
    def isPalindrome(self, s: str) -> bool:
## APPROACH ONE-----------------------------------------------------------------------
        # finalStr = ""
        # for x in s.lower():
        #     if ord(x) in range(97,123) or ord(x) in range(48,58) :
        #         finalStr+=x


        # # print(finalStr)
        # return(finalStr == finalStr[::-1])

## APPROACH TWO-----------------------------------------------------------------------
        i=0
        j=len(s)-1

        while i<j:
            print(s[i],s[j])
            if s[i].isalnum()==False:
                i+=1
            elif s[j].isalnum()==False:
                j-=1
            elif s[i].lower()!=s[j].lower():
                return False
            elif s[i].lower()==s[j].lower():
                i+=1
                j-=1
        return True
            

