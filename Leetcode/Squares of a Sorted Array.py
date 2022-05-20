class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        A.sort()
        ls = []
        
        for i in A:
            i = i**2
            ls.append(i)
            
        ls.sort()
        return ls