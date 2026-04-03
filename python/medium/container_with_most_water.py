from typing import List 

class Solution:
  def maxArea(self, height: List[int]) -> int:
    left, right = 0, len(height) - 1
    maxA = 0

    while left < right:
      area = (right - left) * min(height[right], height[left])
      maxA = max(area, maxA)

      if height[left] < height[right]:
        left += 1
      else:
        right -= 1
    
    return maxA
   
sol = Solution()
 
test1 = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(f"Output of test1: {test1}\n")
test2 = sol.maxArea([1,1])
print(f"Output of test2: {test2}\n")