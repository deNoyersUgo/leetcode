class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
        
        
sol = Solution()

test1 = sol.lengthOfLastWord("Hello World")
print(f"Output of test1: {test1}\n")
test2 = sol.lengthOfLastWord("   fly me   to   the moon  ")
print(f"Output of test2: {test2}\n")
test3 = sol.lengthOfLastWord("luffy is still joyboy")
print(f"Output of test3: {test3}\n")