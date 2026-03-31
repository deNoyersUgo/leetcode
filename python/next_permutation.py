from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
      
        pivot_index = -1
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot_index = i
                break
      
        if pivot_index != -1:  # Using explicit comparison instead of ~i bitwise operation
            swap_index = -1
            for j in range(n - 1, pivot_index, -1):
                if nums[j] > nums[pivot_index]:
                    swap_index = j
                    break
          
            nums[pivot_index], nums[swap_index] = nums[swap_index], nums[pivot_index]
      
        left = pivot_index + 1
        right = n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        
test1 = Solution().nextPermutation([1,2,3])
print(f"Output of test1: {test1}\n")
test2 = Solution().nextPermutation([3,2,1])
print(f"Output of test2: {test2}\n")
test3 = Solution().nextPermutation([1,1,5])
print(f"Output of test3: {test3}\n")