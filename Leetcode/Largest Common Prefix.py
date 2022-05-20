class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        strs.sort(reverse=False)
        print(strs)
        
        templist = [strs[0],strs[-1]]
        prefix = []
        
        for i in range(0,len(min(templist,key = len))):
            if templist[0][i] == templist[1][i]:
                prefix.append(templist[0][i])
            else:
                break
                
        return "".join(prefix)