from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 0: 
            return 1
            
        indicator = []
        for _ in range(0, n+1):
            indicator.append(0)
        
        for i in range(0, n):
            if nums[i] >= 0  and nums[i] <= n:
                indicator[nums[i]] = 1
                
        for i in range(1, n+1):
            if indicator[i] == 0:
                return i
        
        return n+1
        
            

        
test1 = Solution().firstMissingPositive([1,2,0])
print(f"Output of test1: {test1}\n")
test2 = Solution().firstMissingPositive([3,4,-1,1])
print(f"Output of test2: {test2}\n")
test3 = Solution().firstMissingPositive([7,8,9,11,12])
print(f"Output of test3: {test3}\n")