from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(idx: int) -> None:
            # base case
            if idx == length:
                result.append(current_permutation[:])
                return
            
            for j in range(length):
                if visited[j]:
                    continue
                    
                if j > 0 and nums[j] == nums[j-1] and not visited[j-1]:
                    continue
                
                current_permutation[idx] = nums[j]
                visited[j] = True
                
                backtrack(idx + 1)
                
                visited[j] = False
                
        length = len(nums)
        nums.sort()
        result = []
        current_permutation = [0] * length
        visited = [False] * length
        
        backtrack(0)
        
        return result
                

sol = Solution()
        
test1 = sol.permuteUnique([1,1,2])
print(f"Output of test1: {test1}\n")
test2 = sol.permuteUnique([1,2,3])
print(f"Output of test2: {test2}\n")
