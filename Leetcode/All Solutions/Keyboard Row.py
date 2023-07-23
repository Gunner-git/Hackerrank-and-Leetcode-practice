class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = "qwertyuiop"
        secondRow = "asdfghjkl"
        thirdRow = "zxcvbnm"
        
        res = []
        
        for word in words:
            flagRow1 = True
            flagRow2 = True
            flagRow3 = True
            
            lowerWord = word.lower()
            for i in lowerWord:
                if i not in firstRow:
                    flagRow1 = False
            for j in lowerWord:
                if j not in secondRow:
                    flagRow2 = False
            for k in lowerWord:
                if k not in thirdRow:
                    flagRow3 = False
            
            if flagRow1 == True:
                print(word)
                res.append(word)
            elif flagRow2 == True:
                res.append(word)
            elif flagRow3 == True:
                res.append(word)
                
        return res