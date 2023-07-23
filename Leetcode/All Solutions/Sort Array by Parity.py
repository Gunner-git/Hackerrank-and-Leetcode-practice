class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        _even = []
        _odd = []
        res = []
        n = len(nums)
        i = 0
        j = 0
        
        
        for i in nums:
            if i%2==0:
                _even.append(i)
            else:
                _odd.append(i)
                
        index = 0
        i = 0
        j = 0

        flag = True

        # Start rearranging array
        while (index < n):

            # If first element is even
            if (flag == True):
                nums[index] = _even[i]
                index += 1
                i += 1
                flag = ~flag

            # Else, first element is Odd
            else:
                nums[index] = _odd[j]
                index += 1
                j += 1
                flag = ~flag

        # Print the rearranged array
        for i in range(n):
            res.append(nums[i])
            
        return res
        