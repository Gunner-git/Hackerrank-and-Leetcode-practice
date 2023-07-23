class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        listSentence = s.split(" ")
        for i in range(0,len(listSentence)- k):
            listSentence.pop()
        res = " ".join(listSentence)
        return res