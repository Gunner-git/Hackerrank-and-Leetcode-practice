class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        for i in range(0,length):
            nums.append(nums[i])

        return nums