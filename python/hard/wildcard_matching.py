class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        i, j =0, 0
        star, sp = -1, -1
        
        while i < m:
            if j < n and (p[j] == "?" or s[i] == p[j]):
                i += 1
                j += 1
            
            elif j < n and p[j] == '*':
                star = j
                sp = i
                j += 1
                
            elif star != -1:
                j = star + 1
                sp += 1
                i = sp
            
            else: 
                return False
                
        while j < n and p[j] == '*':
            j += 1
        
        return j == n
            
sol = Solution()
        
test1 = sol.isMatch("aa", "a")
print(f"Output of test1: {test1}\n")
test2 = sol.isMatch("aa", "*")
print(f"Output of test2: {test2}\n")
test3 = sol.isMatch("cb", "?a")
print(f"Output of test3: {test3}\n")