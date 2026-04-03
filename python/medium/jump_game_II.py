from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        print(f"n = {n}")
        
        if n < 2:
            return 0
        
        max_reach, steps, end = 0, 0, 0
        
        for i in range(n-1):
            max_reach = max(max_reach, i + nums[i])
            print(f"i = {i} and max_reach = {max_reach}")
            
            if i == end:
                end = max_reach
                steps += 1
        
        return steps
        
sol = Solution()            
                    
test1 = sol.jump([2,3,1,1,4])
print(f"Output of test1: {test1}\n")
test2 = sol.jump([2,3,0,1,4])
print(f"Output of test2: {test2}\n")