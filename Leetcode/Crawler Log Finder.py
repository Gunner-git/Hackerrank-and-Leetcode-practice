class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        
        for command in logs:
            if command == "../":
                if count == 0:
                    pass
                else:
                    count -= 1
            elif command == "./":
                pass
            else:
                count += 1
        
        return count