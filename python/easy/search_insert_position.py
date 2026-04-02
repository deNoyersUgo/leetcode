from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while low < high:
            mid = (high + low) // 2
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid
        
        return low
        
            
        
        
test1 = Solution().searchInsert([1,3,5,6],5)
print(f"Output of test1: {test1}\n")
test2 = Solution().searchInsert([1,3,5,6],2)
print(f"Output of test2: {test2}\n")
test3 = Solution().searchInsert([1,3,5,6],7)
print(f"Output of test3: {test3}\n")