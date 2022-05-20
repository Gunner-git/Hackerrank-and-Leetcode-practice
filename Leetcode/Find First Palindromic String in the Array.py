class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            _list = [j for j in i]
            check = False
            palindrome = True
            
            k = 0
            l = len(i)-1

            while check == False:
                if k > (len(i)-1)//2 or l < (len(i)-1)//2 or l==k:
                    check = True
                if _list[k] == _list[l]:
                    k += 1
                    l -= 1
                else:
                    palindrome = False
                    check = True
            
            if palindrome == True:
                return i
        return ""