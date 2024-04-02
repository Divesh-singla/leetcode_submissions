class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for x in operations:
            if x[1]=="+":
                result+=1
            else:
                result-=1
        return result