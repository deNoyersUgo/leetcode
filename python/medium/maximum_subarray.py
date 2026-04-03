from typing import List 

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0]
        
        for num in nums[1:]:
            current_sum = max(current_sum, 0) + num
            max_sum = max(max_sum, current_sum)
            
        return max_sum
        
sol = Solution()

test1 = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(f"Output of test1: {test1}\n")
test2 = sol.maxSubArray([1])
print(f"Output of test2: {test2}\n") 
test3 = sol.maxSubArray([5,4,-1,7,8])
print(f"Output of test3: {test3}\n") 