class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        split = []
        count = 0
        for i in sentences:
            split.append(i.split(" "))
        for j in split:
            if len(j) >= count:
                count = len(j)
        return count
