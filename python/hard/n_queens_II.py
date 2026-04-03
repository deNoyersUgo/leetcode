class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int) -> None:
            # base case: all queens are successfully placed
            if row == n:
                nonlocal solution_count
                solution_count += 1
                return
            
            # try placing a queen in each column of the current row    
            for col in range(n):
                # check if placing queen at (row, col) is safe
                if (columns_used[col] == 0) and diagonals_used[row + col] == 0 and anti_diagonals_used[n - row + col] == 0:
                    

                    # mark the column and diagnols as occupied
                    columns_used[col] = 1
                    diagonals_used[row + col] = 1
                    anti_diagonals_used[n - row + col] = 1
                    
                    # recursively place queens in the next row
                    backtrack(row + 1)
                    
                    # backtrack: remove the queen and unmark the positions
                    columns_used[col] = 0
                    diagonals_used[row + col] = 0
                    anti_diagonals_used[n - row + col] = 0
                    
                            
        # track which columns are occupied by queens
        columns_used = [0] * n
        
        # Track which diagonals are occupied (row + col identifies each diagonal)
        # Maximum possible value is (n-1) + (n-1) = 2n-2, so we need 2n-1 elements
        diagonals_used = [0] * (2 * n)
              
        # Track which anti-diagonals are occupied (n - row + col identifies each anti-diagonal)
        # Range is from n - (n-1) + 0 = 1 to n - 0 + (n-1) = 2n-1, so we need 2n elements
        anti_diagonals_used = [0] * (2 * n)
        
        # counter for total number of valid solutions
        solution_count = 0
              
        # Start the backtracking from row 0
        backtrack(0)
              
        return solution_count

sol = Solution()    

test1 = sol.totalNQueens(4)
print(f"Output of test1: {test1}\n")
test2 = sol.totalNQueens(1)
print(f"Output of test2: {test2}\n")