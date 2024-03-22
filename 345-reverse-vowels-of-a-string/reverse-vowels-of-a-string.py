class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o',"u"]
        value = []
        index = []
        sList = list(s)
        result = ""

        for x in range(len(s)):
            if s[x].lower() in vowels:
                index.append(x)
                value.append(s[x])
        
        index = index[::-1]

        for y in range(len(index)):
            sList[index[y]] = value[y]

        return "".join(sList)

# ---------------------online solution ------------------------------------
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         l = 0
#         r = len(s) - 1
#         vowels = ['a', 'e', 'i', 'o', 'u']
#         s = list(s)
#         while (l < r):
#             if s[l].lower() not in vowels:
#                 l += 1
#             elif s[r].lower() not in vowels:
#                 r -= 1
#             else:
#                 s[l], s[r] = s[r], s[l]
#                 l += 1
#                 r -= 1
#         return "".join(s)