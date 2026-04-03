from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        left, right = 0, len(matrix) - 1
       
        while left < right:
            for i in range(right - left) :
                top, bottom = left, right
                
                topLeft = matrix[top][left + i]
                
                matrix[top][left + i] = matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] = topLeft
                
            right -= 1
            left += 1
                    
sol = Solution()
        
test1 = sol.rotate([[1,2,3],[4,5,6],[7,8,9]])
print(f"Output of test1: {test1}\n")
test2 = sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])
print(f"Output of test2: {test2}\n")