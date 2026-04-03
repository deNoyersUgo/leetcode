from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Track the maximum index we can reach so far
        max_reachable = 0
      
        # Iterate through each position and its jump value
        for current_pos, jump_length in enumerate(nums):
            # If current position is beyond our maximum reach, we can't proceed
            if max_reachable < current_pos:
                return False
          
            # Update the maximum reachable index
            # Current position + jump length gives us the farthest we can go from here
            max_reachable = max(max_reachable, current_pos + jump_length)
      
        # If we've gone through all positions without getting stuck, we can reach the end
        return True

sol = Solution()

test1 = sol.canJump([2, 3, 1, 1, 4])
print(f"Output of test1: {test1}\n")
test2 = sol.canJump([3, 2, 1, 0, 4])
print(f"Output of test2: {test2}\n")