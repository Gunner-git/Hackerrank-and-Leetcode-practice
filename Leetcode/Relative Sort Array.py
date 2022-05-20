class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ls = []
        ls2 = []
        
        for i in arr2:
            for j in arr1:
                if j == i:
                    ls.append(j)
        
        for l in arr1:
            if l not in ls:
                ls2.append(l)
                
        ls2.sort()
        
        for k in ls2:
            ls.append(k)
        
        return ls