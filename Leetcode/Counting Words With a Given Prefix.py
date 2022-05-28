class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count = 0
        
        for i in words:
            if len(i)>=len(pref):
                
                firstTwoLetters = ''

                for j in range(0,len(pref)):
                    firstTwoLetters += i[j]

                print(firstTwoLetters)

                if pref == firstTwoLetters:
                    count += 1

        return count