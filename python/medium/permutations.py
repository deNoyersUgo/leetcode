from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)
        
        def dfs(path: List[int]) -> None:
            if len(path) == len(nums):
                res.append(path.copy())
                return
            
            for i, num in enumerate(nums):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(num)
                dfs(path)
                path.pop()
                used[i] = False
                
        dfs([])
        return res

        
test1 = Solution().permute([1,2,3])
print(f"Output of test1: {test1}\n")
test2 = Solution().permute([0,1])
print(f"Output of test2: {test2}\n")
test3 = Solution().permute([1])
print(f"Output of test3: {test3}\n")