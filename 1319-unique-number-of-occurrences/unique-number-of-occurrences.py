class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        dicct = {}
        
        seet = set()
        for x in arr:
            if x in dicct.keys():
                dicct[x] += 1

            else:
                dicct[x] = 1
        
        for key,value in dicct.items():
            
            seet.add(value)
        

        if len(arr) == sum(seet):
            return True
        else:
            return False
        
        