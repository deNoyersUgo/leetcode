from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        first, last = -1, -1
        
        while lo<= hi:
            mid = (hi+lo) // 2
            
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid-1
            else:
                hi = mid-1
                first= mid
        
        
        lo, hi = 0, len(nums) - 1
        
        while lo <= hi:
            mid =  (hi+lo) // 2
           
            if nums[mid] < target:
                lo = mid+1
            elif nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
                last = mid
        
        return [first, last]
        
sol = Solution()  
        
test1 = sol.searchRange([5,7,7,8,8,10],8)
print(f"Output of test1: {test1}\n")
test2 = sol.searchRange([5,7,7,8,8,10],6)
print(f"Output of test2: {test2}\n")
test3 = sol.searchRange([],0)
print(f"Output of test3: {test3}\n")