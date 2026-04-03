
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Handle edge cases
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10
                        
        # For odd-length numbers, the middle digit is irrelevant, so we can ignore it
        return x == reversed_half or x == reversed_half // 10
     
sol = Solution()

test1 = sol.isPalindrome(121)
print(f"Output of test1: {test1}\n")
test2 = sol.isPalindrome(-121)
print(f"Output of test2: {test2}\n")
test3 = sol.isPalindrome(10)
print(f"Output of test3: {test3}\n")
