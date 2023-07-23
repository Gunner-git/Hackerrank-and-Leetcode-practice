class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        output = []

        for word in words:
            flag1 = 0
            flag2 = 0
            flag3 = 0

            test_word = word.lower()
            
            for letter1 in test_word:
                if letter1 not in "qwertyuiop":
                    flag1 = 1
            
            for letter2 in test_word:
                if letter2 not in "asdfghjkl":
                    flag2 = 1
            
            for letter3 in test_word:
                if letter3 not in "zxcvbnm":
                    flag3 = 1

            if flag1 == 0 or flag2 == 0 or flag3 == 0:
                output.append(word)

            print(output)

        return output