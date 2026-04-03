from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        lMax, rMax = 0, 0
        res = 0
        
        while left < right:
            if height[left] < height[right]:
                lMax = max(lMax, height[left])
                res += lMax - height[left]
                left += 1
            else:
                rMax = max(rMax, height[right])
                res += rMax - height[right]
                right -= 1
        
        return res
            
sol = Solution()
        
test1 = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(f"Output of test1: {test1}\n")
test2 = sol.trap([4,2,0,3,2,5])
print(f"Output of test2: {test2}\n")