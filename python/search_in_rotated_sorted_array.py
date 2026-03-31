from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right =  0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
                
            # Check which half is sorted
            if nums[left] <= nums[mid]:
                # Left Half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            else:
            # Right Half is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1 
                else:
                    right = mid - 1
        return -1
        
            
        
        
test1 = Solution().search([4,5,6,7,0,1,2],0)
print(f"Output of test1: {test1}\n")
test2 = Solution().search([4,5,6,7,0,1,2],3)
print(f"Output of test2: {test2}\n")
test3 = Solution().search([1],0)
print(f"Output of test3: {test3}\n")