class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        
        # Language specific approach
        strWord1 = "".join(word1)
        strWord2 = "".join(word2)
        
        if strWord1 == strWord2:
            return True
        return False

        # Generic approach
        # strWord1 = ''
        # strWord2 = ''
        
        # for i in word1:
        #     strWord1 += i
        # for j in word2:
        #     strWord2 += j
        
        # print(strWord1, strWord2)
        # if strWord1 == strWord2:
        #     return True
        # return False