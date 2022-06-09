class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        count = 0
        
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    print((nums[i],nums[j]))
                    count += 1

        return count