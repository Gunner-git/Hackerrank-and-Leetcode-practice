class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsTruncated = set(nums)
        numsTruncated = list(numsTruncated)
        print(numsTruncated)
        
        nums.sort()
        numsTruncated.sort()
        
        if numsTruncated == nums:
            return False
        else:
            return True