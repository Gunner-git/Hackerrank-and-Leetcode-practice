class Solution:
    def romanToInt(self, s: str) -> int:
        
        sum = 0
        flag = False
        romanDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        letterList = [i for i in s]
        
        for index in range(0,len(letterList)):
            if flag == False:
                if index < len(letterList)-1:
                    if romanDict[letterList[index]] < romanDict[letterList[index+1]]:
                        sum += (romanDict[letterList[index+1]] - romanDict[letterList[index]])
                        flag = True
                    else:
                        sum += romanDict[letterList[index]]
                else:
                    sum += romanDict[letterList[index]]
            else:
                flag = False

            
        return sum