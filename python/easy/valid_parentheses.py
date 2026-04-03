class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        
        return not stack
        
sol = Solution()
        
test1 = sol.isValid("()")
print(f"Output of test1: {test1}\n")
test2 = sol.isValid("()[]{}")
print(f"Output of test2: {test2}\n")
test3 = sol.isValid("(]")
print(f"Output of test3: {test3}\n")
test4 = sol.isValid("([])")
print(f"Output of test4: {test4}\n")
test5 = sol.isValid("([)]")
print(f"Output of test5: {test5}\n")