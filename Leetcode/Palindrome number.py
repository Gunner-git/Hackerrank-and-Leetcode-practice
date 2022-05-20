def isPalindrome(x):
    # Solution
    s = str(x)
    
    if '-' in s:
        return False
    else:
        l = [int(i) for i in s]
        a = [int(j) for j in s]
        a.reverse()

    if l == a:
        return True
    else:
        return False


# Test input in leetcode for this problem
x = 121

# Calling the function
isPalindrome(x)