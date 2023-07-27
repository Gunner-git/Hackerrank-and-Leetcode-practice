class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arrayS = [i for i in s]
        arrayT = [j for j in t]

        arrayS.sort()
        arrayT.sort()

        if arrayS == arrayT:
            return True
        else:
            return False
