from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # get matrix dimensions
        num_rows, num_cols = len(matrix), len(matrix[0])
        
        # direction vectors: right(0,1), down(1,0), left(0,-1), up(-1,0)
        # stored as (dx1, dy1, dx2, dy2, dx3, dy3, dx4, dy4) in compressed form
        directions = [0, 1, 0, -1, 0]
        
        # track visited cells to know when to turn 
        visited = [[False] * num_cols for _ in range(num_rows)]
        
        # initialize position (row, col) and direction index
        row = col = direction_idx = 0
        result = []
        
        # traverse all cells in the matrix
        for _ in range(num_rows * num_cols):
            result.append(matrix[row][col])
            visited[row][col] = True
            
            # calculate next position based in current direction
            next_row = row + directions[direction_idx]
            next_col = col + directions[direction_idx + 1]
            
            # check if we nee dto change direction (hit boundary or visited cell)
            if (next_row < 0 or next_row >= num_rows or 
                next_col < 0 or next_col >= num_cols or 
                visited[next_row][next_col]):
                # Turn clockwise (right -> down -> left -> up -> right)
                direction_idx = (direction_idx + 1) % 4
                
            # Move to next position using current (possibly updated) direction
            row += directions[direction_idx]
            col += directions[direction_idx + 1]
        return result
        
sol = Solution()

test1 = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(f"Output of test1: {test1}\n")
test2 = sol.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(f"Output of test2: {test2}\n") 