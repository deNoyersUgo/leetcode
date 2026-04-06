from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # get matrix dimensions
        matrix = [[0] * n for _ in range(n)]
        directions = [0, 1, 0, -1, 0]
        row = col = 0
        direction_idx = 0 # we start moving to the right
        
        for value in range(1, n*n +1):
            matrix[row][col] = value
            
            next_row = row + directions[direction_idx]
            next_col = col + directions[direction_idx + 1]
            
            if (next_row < 0 or next_row >= n or 
                next_col < 0 or next_col >= n or
                matrix[next_row][next_col] != 0):
                direction_idx = (direction_idx + 1)%4
                    
            
            
            row += directions[direction_idx]
            col += directions[direction_idx + 1]
                
        return matrix
    
sol = Solution()

test1 = sol.generateMatrix(3)
print(f"Output of test1: {test1}\n")
test2 = sol.generateMatrix(1)
print(f"Output of test2: {test2}\n") 