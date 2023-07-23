class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2: return 0
        nonprimes = set()
        for i in range(2, round(n**(1/2))+1):
            if i not in nonprimes:
                for j in range(i*i, n, i):
                    nonprimes.add(j)
        return n - len(nonprimes) - 2
        
#         prime = 0
#         flag = False
        
#         if n <= 2:
#             return 0
#         elif n ==3:
#             return 1
#         else:     
#             for i in range(n-1,1,-1):
#                 flag = False
#                 for j in range(i-1,1,-1):
#                     if (i%j)==0:
#                         flag = True
#                         break
#                 if flag == False:
#                     prime += 1

#         return prime