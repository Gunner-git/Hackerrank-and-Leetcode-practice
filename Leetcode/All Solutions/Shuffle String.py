class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        newString = [j for j in s]
        count = 0
        for i in s:
            newString[indices[count]] = i
            count += 1
        return "".join(newString)