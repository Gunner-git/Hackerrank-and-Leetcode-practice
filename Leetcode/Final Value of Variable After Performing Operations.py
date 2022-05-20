class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        res = 0
        for i in operations:
            if i == '++X' or i == 'X++':
                res = res + 1
            else:
                res = res - 1
        return res