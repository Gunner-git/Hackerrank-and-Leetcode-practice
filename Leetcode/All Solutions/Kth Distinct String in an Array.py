class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        distinctList = []
        
        for i in arr:
            if arr.count(i) == 1:
                distinctList.append(i)
        
        if len(distinctList)-1 >= k-1:
            return distinctList[k-1]
        else:
            return ""