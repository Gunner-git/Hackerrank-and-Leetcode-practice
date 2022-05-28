class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        firstLetters = ''
        count = 0
        
        for i in s:
            firstLetters += i
            
            for pref in words:
                if pref == firstLetters:
                    count += 1
        
        return count