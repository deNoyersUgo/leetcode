from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        # We use a mutable list as a stateful stack to track our sequence.
        # This completely bypasses the memory allocation overhead of string concatenation.
        current_sequence = []

        def backtrack(open_count: int, close_count: int):
            # Base case: Mathematically, a valid sequence contains exactly 2n characters.
            if len(current_sequence) == 2 * n:
                # We execute a single C-level join operation only when a valid leaf node is reached.
                ans.append("".join(current_sequence))
                return

            # We can place an open parenthesis strictly if we haven't exhausted our pool of 'n'.
            if open_count < n:
                current_sequence.append('(')
                backtrack(open_count + 1, close_count)
                # We revert the state to backtrack mathematically up the tree,
                # leaving the memory register ready for the alternate branch.
                current_sequence.pop()

            # We can place a close parenthesis strictly if it mathematically balances 
            # an unclosed open parenthesis currently on the stack.
            if close_count < open_count:
                current_sequence.append(')')
                backtrack(open_count, close_count + 1)
                # We pop again to restore the exact state for any prior caller.
                current_sequence.pop()

        backtrack(0, 0)
        return ans
        
test1 = Solution().generateParenthesis(3)
print(f"Output of test1: {test1}\n")
test2 = Solution().generateParenthesis(1)
print(f"Output of test2: {test2}\n")
