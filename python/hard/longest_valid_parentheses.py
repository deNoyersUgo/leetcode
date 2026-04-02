class Solution:
    def longestValidParentheses(self, s: str) -> int:
        arr = [-1] #push -1 onto the staclk as initial value
        result = 0
        
        if s == "": #handle empty string case
            return 0
            
        for i in range(len(s)):
            if s[i] == "(":
                arr.append(i)
            else:
                arr.pop()
                if  len(arr) != 0: #stack not empty
                    result = max(result, i-arr[len(arr)-1]) # total length is updated
                else: #stack is empty
                    arr.append(i)
        return result
            
        
        
test1 = Solution().longestValidParentheses("(()")
print(f"Output of test1: {test1}\n")
test2 = Solution().longestValidParentheses(")()())")
print(f"Output of test2: {test2}\n")
test3 = Solution().longestValidParentheses("")
print(f"Output of test3: {test3}\n")