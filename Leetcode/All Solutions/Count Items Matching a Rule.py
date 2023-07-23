class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        res = 0
        
        # My code
#         for i in items:
#             if ruleKey == "color":
#                 if i[1] == ruleValue:
#                     res = res + 1
#                     print(res)
#             elif ruleKey == 'type':
#                 if i[0] == ruleValue:
#                     res = res + 1
#                     print(res)
#             elif ruleKey == 'name':
#                 if i[2] == ruleValue:
#                     res = res + 1
#                     print(res)
            
#         return res
    
        # better code
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        else:
            idx = 2
        
        for item in items:
            if item[idx] == ruleValue:
                res += 1
        
        return res