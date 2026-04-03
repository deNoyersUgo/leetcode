from typing import List 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        N, quadruplets = len(nums), set()
        
        for i in range(N):
            for j in range(i+1, N):
                left, right = j+1, N-1
                
                # typical two sum strategy
                while left < right:
                    curr_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if curr_sum == target:
                        quadruplets.add((nums[i], nums[j], nums[left], nums[right]))
                        left, right = left + 1, right - 1
                    elif curr_sum < target:
                        left += 1
                    else:
                        right -= 1
        return list(quadruplets)

sol = Solution()        

test1 = sol.fourSum([1,0,-1,0,-2,2], 0)
print(f"Output of test1: {test1}\n")
test2 = sol.fourSum([2,2,2,2,2], 8)
print(f"Output of test2: {test2}\n")