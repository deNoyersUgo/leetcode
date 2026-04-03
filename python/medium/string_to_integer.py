class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in {'-', '+'}:
            s = s[1:]
        num = 0
        for c in s:
            if not c.isdigit():
                break
            num = num * 10 + ord(c) - ord('0')
            if sign * num <= -2**31:
                return -2**31
            if sign * num >= 2**31 - 1:
                return 2**31 - 1
        return sign * num
                
sol = Solution()

test1 = sol.myAtoi("42")
print(f"Output of test1: {test1}\n")
test2 = sol.myAtoi("   -042")
print(f"Output of test2: {test2}\n")
test3 = sol.myAtoi("1337c0d3")
print(f"Output of test3: {test3}\n")
test4 = sol.myAtoi("0-1")
print(f"Output of test2: {test4}\n")
test5 = sol.myAtoi("words and 987")
print(f"Output of test3: {test5}\n")