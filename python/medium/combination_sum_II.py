from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(s: int, target: int, path: List[int]) -> None:
            if target < 0:
                 return 
            if target == 0:
                res.append(path.copy())
                return
                
            for i in range(s, len(candidates)):
                if i > s  and candidates[i] == candidates[i-1]:
                    continue
                path.append(candidates[i])
                dfs(i+1, target-candidates[i], path)
                path.pop()
        candidates.sort()
        dfs(0, target, [])
        return res
            
sol = Solution()
        
test1 = sol.combinationSum2([10,1,2,7,6,1,5], 8)
print(f"Output of test1: {test1}\n")
test2 = sol.combinationSum2([2,5,2,1,2], 5)
print(f"Output of test2: {test2}\n")