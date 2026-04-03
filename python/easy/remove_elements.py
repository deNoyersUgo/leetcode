from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
sol = Solution()

test1 = sol.removeElement([3,2,2,3], 3)
print(f"Output of test1: {test1}\n")
test2 = sol.removeElement([0,1,2,2,3,0,4,2], 2)
print(f"Output of test2: {test2}\n")