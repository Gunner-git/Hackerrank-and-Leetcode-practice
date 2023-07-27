class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        array_nums = [i for i in set_nums]
        
        array_nums.sort()
        nums.sort()

        if array_nums == nums:
            return False
        else:
            return True
