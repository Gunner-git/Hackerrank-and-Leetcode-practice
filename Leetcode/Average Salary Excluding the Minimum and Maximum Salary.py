class Solution:
    def average(self, salary: List[int]) -> float:
        salary.remove(min(salary))
        salary.remove(max(salary))
        
        s = 0
        
        for i in salary:
            s+=i
        
        ans = s/len(salary)
        return ans
        