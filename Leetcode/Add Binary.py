class Solution:
    def addBinary(self, a: str, b: str) -> str:
        l=[]
        x = 0
        y = 0
        
        a_l = [int(j) for j in a]
        a_l.reverse()
        
        b_l = [int(k) for k in b]
        b_l.reverse()
        
        for i in a_l:
            l.append((2**x)*i)
            x+=1
            
        for g in b_l:
            l.append((2**y)*g)
            y+=1
        
        bin_ = bin(sum(l))
        
        ans = [p for p in bin_]
        
        ans.pop(0)
        ans.pop(0)
        
        res = "".join(ans)
        
        return res