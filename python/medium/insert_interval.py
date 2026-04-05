from typing import List
        
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        result = []
        start, end = intervals[0]
        
        for s, e in intervals[1:]:
            # no overlap case
            if end < s:
                result.append([start, end])
                start, end = s, e
            # overlap case
            else:
                end = max(end, e)
            
        result.append([start, end])
        
        return result
        
        
        
        


sol = Solution()

test1 = sol.insert([[1,3],[6,9]], [2,5])
print(f"Output of test1: {test1}\n")
test2 = sol.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8])
print(f"Output of test2: {test2}\n")
