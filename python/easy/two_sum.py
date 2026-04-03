from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # We use a hash map to achieve O(1) average lookup time, 
        # completely eliminating the need for a second nested loop.
        num_map = {}
        
        for i, num in enumerate(nums):
            # We calculate the required mathematical complement first 
            # to verify if we've already seen the number needed to hit the target.
            complement = target - num
            
            # Checking the map before adding the current number guarantees 
            # we do not use the exact same array element twice.
            if complement in num_map:
                return [num_map[complement], i]
            
            # We store the number and its index only after the check.
            # This sequential operation naturally handles edge cases where 
            # the target is made of two identical numbers (e.g., target 6, nums = [3, 3]).
            num_map[num] = i
            
        return []

sol = Solution()

test1 = sol.twoSum([2,7,11,15], 9)
print(f"Output of test1: {test1}")
test2 = sol.twoSum([3, 2, 4], 6)
print(f"Output of test2: {test2}")
test3 = sol.twoSum([3, 3], 6)
print(f"Output of test3: {test3}")