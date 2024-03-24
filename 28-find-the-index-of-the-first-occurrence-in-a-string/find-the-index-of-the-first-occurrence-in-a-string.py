class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        result = []
        for x in range(len(haystack)):
            
            if haystack[x:(x+len(needle))] == needle:
                result.append(x)
                
        if result != []:
            return result[0]
        else:
            return -1
        