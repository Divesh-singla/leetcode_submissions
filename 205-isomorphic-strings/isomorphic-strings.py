class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        map1 = []
        map2 = []
        for x in s:
            map1.append(s.index(x))

        for y in t:
            map2.append(t.index(y))
        print(map1,map2)
        if map1 == map2:
            return True
        else:
            False
