class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        strLen = len(s)
        patternLen = len(p)
        dp = [[False] * (patternLen + 1) for _ in range(strLen + 1)]
        dp[0][0] = True
        
        def matches(strIndex: int, patternIndex: int) -> bool:
            return patternIndex >= 0 and (p[patternIndex] == '.' or s[strIndex] == p[patternIndex])
        for j, c in enumerate(p):
            if c == '*' and dp[0][j-1]:
                dp[0][j+1] = True
                
        for i in range(strLen):
            for j in range(patternLen):
                if p[j] == '*':
                    noRepeat = dp[i+1][j-1]
                    doRepeat = matches(i, j-1) and dp[i][j+1]
                    dp[i+1][j+1] = noRepeat or doRepeat
                elif matches(i,j):
                    dp[i+1][j+1] = dp[i][j]
        return dp[strLen][patternLen]

sol = Solution()

test1 = sol.isMatch("aa", "a")
print(f"Output of test1: {test1}\n")
test2 = sol.isMatch("aa", "a*")
print(f"Output of test2: {test2}\n")
test3 = sol.isMatch("ab", ".*")
print(f"Output of test3: {test3}\n")

class SolutionBis:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        # We instantiate a single 1D array to represent the DP state of the previous string character.
        # This reduces our memory footprint from O(M*N) down to O(N).
        prev = [False] * (n + 1)
        prev[0] = True
        
        # We mathematically seed the base cases for an empty string matching patterns like "a*b*c*".
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                prev[j] = prev[j - 2]
                
        for i in range(1, m + 1):
            # We construct a fresh array for the current character's state evaluation.
            curr = [False] * (n + 1)
            
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    # We evaluate the zero-occurrence case by checking the state two steps back in the pattern.
                    no_repeat = curr[j - 2]
                    
                    # We evaluate the one-or-more occurrence case by ensuring the preceding character matches 
                    # and that the previous string state was valid.
                    do_repeat = prev[j] and (p[j - 2] == s[i - 1] or p[j - 2] == '.')
                    
                    curr[j] = no_repeat or do_repeat
                else:
                    # A direct character match or '.' wildcard propagates the diagonal state mathematically.
                    curr[j] = prev[j - 1] and (p[j - 1] == s[i - 1] or p[j - 1] == '.')
            
            # We overwrite the previous state with the current state, rolling the active window forward.
            prev = curr
            
        return prev[n]