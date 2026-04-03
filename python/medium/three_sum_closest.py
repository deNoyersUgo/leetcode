from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        
        for i in range(len(nums)-2):
            left, right = i+1, len(nums)-1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                
                if s == target:
                   return s
                
                if abs(s-target) < abs(res-target):
                   res = s 
                   
                if s < target:
                    left += 1
                else: 
                    right -= 1
                    
        return res
        
sol = Solution()

test1 = sol.threeSumClosest([-1,2,1,-4], 1)
print(f"Output of test1: {test1}\n")
test2 = sol.threeSumClosest([0,0,0], 1)
print(f"Output of test2: {test2}\n")