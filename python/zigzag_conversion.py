class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # We immediately return if the geometry does not permit a zigzag.
        # This prevents division-by-zero errors in our cycle calculation.
        if numRows == 1 or numRows >= len(s):
            return s

        # We pre-allocate a single flat list for character collection.
        # Joining an array of characters once at the end is strictly faster 
        # than repeated string concatenations.
        result = []
        
        # We define the mathematical length of one complete cycle (down and diagonally up).
        cycle_len = 2 * numRows - 2

        for i in range(numRows):
            # We stride through the original string jumping exactly one full cycle at a time,
            # ensuring cache-friendly sequential reading.
            for j in range(i, len(s), cycle_len):
                
                # The primary vertical column character is unconditionally added.
                result.append(s[j])
                
                # For inner rows, we calculate the exact index of the diagonal character.
                # The condition verifies we are not on the top/bottom rows and prevents out-of-bounds access.
                diagonal_idx = j + cycle_len - 2 * i
                if i != 0 and i != numRows - 1 and diagonal_idx < len(s):
                    result.append(s[diagonal_idx])

        # We execute a single C-level string join operation to generate the final output.
        return "".join(result)
      
test1 = Solution().convert("PAYPALISHIRING", 3)
print(f"Output of test1: {test1}\n")
test2 = Solution().convert("PAYPALISHIRING", 4)
print(f"Output of test2: {test2}\n")
test3 = Solution().convert("A", 1)
print(f"Output of test3: {test3}\n")