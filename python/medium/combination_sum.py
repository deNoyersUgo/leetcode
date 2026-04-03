from typing import List

class Solution:
    def findCombination(self, idx, target, arr, res, ds):
        # base case: all element sin the array have been considered
        if idx == len(arr):
            if target == 0:
                res.append(list(ds))
            return 
            
        # recursive case: pick array element if it's less than or equal to the target
        if arr[idx] <= target:
            ds.append(arr[idx])
            self.findCombination(idx, target - arr[idx],  arr, res, ds) # allow repated elemements by continuing with the same index
            ds.pop() # Backtrack by removing the last added element
            
        # Skip current element and move to the next index
        self.findCombination(idx + 1, target, arr, res, ds)
        
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = [] # store the result
        ds = [] # store a ciurrent combination
        self.findCombination(0, target, candidates, res, ds) # start recursive search
        return res

sol = Solution()     
        
test1 = sol.combinationSum([2,3,6,7], 7)
print(f"Output of test1: {test1}\n")
test2 = sol.combinationSum([2,3,5], 8)
print(f"Output of test2: {test2}\n")
test3 = sol.combinationSum([2], 1)
print(f"Output of test3: {test3}\n")