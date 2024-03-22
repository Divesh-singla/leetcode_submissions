class Solution:
    def reverseWords(self, s: str) -> str:
        arr = []
        inter = ""
        result = ""
        i = 0
        status = 1

        while status:

            if s[i]==" ":
                if len(inter)!=0:
                    arr.append(inter)
                    inter=""
            else:
                inter+=s[i]

            if len(s)-1 == i:
                if (len(inter))>0:
                    arr.append(inter)
                status = 0
            i+=1



        arr = arr[::-1]

        for y in arr:
            result += f"{y} "

        return result[:-1]