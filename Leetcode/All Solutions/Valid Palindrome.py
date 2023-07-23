class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Defining variables
        letters = ""
        str1 = ""
        str2 = ""
        
        # Making a string only containing lowercase alphanumeric characters
        for word in s.split(" "):
            word = word.lower()
            for letter in word:
                if letter in "qwertyuiopasdfghjklzxcvbnm1234567890":
                    letters += letter
        
        # First half of the string
        for i in range(0,len(letters)//2):
            str1 += letters[i]
        
        # Second half of the string
        if len(letters)%2 == 1:
            # If the length of the string is odd, the first letter gets eliminated
            for j in range((len(letters)//2)+1, len(letters)):
                str2 += letters[j]
        else:
            # If it is even, both halves should be the same
            for j in range(len(letters)//2, len(letters)):
                str2 += letters[j]
        
        # Comparing the first half of the string to the reversed second half of the string
        if str1 == str2[::-1]:
            return True
        return False
