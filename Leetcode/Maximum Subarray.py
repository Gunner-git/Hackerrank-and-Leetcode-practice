class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        max_val = nums[0]
        
        prev_best = nums[0]
        
        
        for num in nums[1:]:
            
            prev_best = max(num, num+prev_best)
            max_val = max(max_val, prev_best)
        return max_val
        