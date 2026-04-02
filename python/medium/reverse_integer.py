class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))
        y = y.strip()
        y = y[::-1]
        output = int(y)
        if output >= 2** 31 -1 or output <= -2** 31:
            return 0
        elif x < 0:
           return -1 * output
        else:
           return output
        
test1 = Solution().reverse(123)
print(f"Output of test1: {test1}\n")
test2 = Solution().reverse(-123)
print(f"Output of test2: {test2}\n")
test3 = Solution().reverse(120)
print(f"Output of test3: {test3}\n")