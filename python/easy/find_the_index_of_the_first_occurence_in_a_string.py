class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        hay_len = len(haystack)
        needle_len = len(needle)
        
        for i in range(hay_len - needle_len + 1):
            if haystack[i:i + needle_len] == needle:
                return i
        return -1
   
sol = Solution()

test1 = sol.strStr("sadbutsad", "sad")
print(f"Output of test1: {test1}\n")
test2 = sol.strStr("leetcode", "leeto")
print(f"Output of test2: {test2}\n")