class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        if len(word1) == len(word2)==0:
            return ""
        elif len(word1) == len(word2):
            for x in range (len(word1)):
                result+=word1[x]
                result+=word2[x]

        elif len(word1)>len(word2):
            for x in range(len(word2)):
                result+=word1[x]
                result+=word2[x]
            result+=word1[len(word2):]

        elif len(word1)<len(word2):
            for x in range(len(word1)):
                result+=word1[x]
                result+=word2[x]
            result+=word2[len(word1):]

        elif len(word2)==0:
            return word1

        elif len(word1) ==0 :
            return word2
        return result


