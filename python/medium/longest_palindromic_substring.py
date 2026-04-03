class Solution:
    def longestPalindrome(self, s: str) -> str:
        # We initialize boundaries to track the mathematical slice of the longest palindrome 
        # instead of storing multiple strings in memory, reducing space complexity to O(1).
        start, end = 0, 0

        for i in range(len(s)):
            # We expand around a single character to find odd-length palindromes.
            len1 = self.expand_around_center(s, i, i)
            # We expand around a pair of identical adjacent characters to find even-length palindromes.
            len2 = self.expand_around_center(s, i, i + 1)
            
            # We extract the maximum mathematical length found at this geometric center 
            # to determine if our global maximum boundaries need updating.
            max_len = max(len1, len2)
            
            if max_len > end - start:
                # We recalculate the left boundary purely mathematically based on the center index 
                # and the half-length of the newly discovered maximum palindrome.
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        # We slice the string exactly once at the very end to return the final result.
        return s[start:end + 1]

    def expand_around_center(self, s: str, left: int, right: int) -> int:
        # We enforce boundary conditions safely and verify structural symmetry 
        # before expanding the pointers outward.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        # We return the absolute length of the valid palindrome bounds.
        # The -1 corrects for the final while-loop iteration that breaks the symmetry.
        return right - left - 1
    
sol = Solution()            
            
test1 = sol.longestPalindrome("babad")
print(f"Output of test1: {test1}\n")
test2 = sol.longestPalindrome("cbbd")
print(f"Output of test2: {test2}\n")
