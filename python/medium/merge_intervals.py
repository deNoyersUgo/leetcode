from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
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

test1 = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(f"Output of test1: {test1}\n")
test2 = sol.merge([[1, 4], [4, 5]])
print(f"Output of test2: {test2}\n")
test3 = sol.merge([[4, 7], [1, 4]])
print(f"Output of test3: {test3}\n")
