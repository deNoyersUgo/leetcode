class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        result = []
        used = [False] * (n+1)
        
        for position in range(n):
            factorial = 1
            
            for i in range(1, n - position):
                factorial *= i
                
            for digit in range(1, n+1):
                if not used[digit]:
                    if k > factorial:
                        k -= factorial
                    else:
                        result.append(str(digit))
                        used[digit] = True
                        break
            
        return ''.join(result)

sol = Solution()

test1 = sol.getPermutation(3,3)
print(f"Output of test1: {test1}\n")
test2 = sol.getPermutation(4,9)
print(f"Output of test2: {test2}\n")
test3 = sol.getPermutation(3,1)
print(f"Output of test2: {test3}\n")