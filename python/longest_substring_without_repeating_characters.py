class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # We use a hash map to store the most recent index of each character.
        # This achieves O(1) lookups and eliminates the need for string searches.
        char_map = {}
        max_len = 0
        left = 0
        
        for right, char in enumerate(s):
            # If we encounter a duplicate AND its previous occurrence is inside our current window,
            # we instantly shift the left boundary just past that previous occurrence.
            # This prevents us from counting the duplicate twice and maintains a valid window.
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # We unconditionally update the dictionary with the current character's new index.
            # This ensures future collisions reference the most up-to-date position.
            char_map[char] = right
            
            # We calculate the window size mathematically (right - left + 1) 
            # rather than maintaining and measuring a physical string in memory.
            max_len = max(max_len, right - left + 1)
            
        return max_len
            
     
        

test1 = Solution().lengthOfLongestSubstring("abcabcbb")
print(f"Output of test1: {test1}\n")
test2 = Solution().lengthOfLongestSubstring("bbbbb")
print(f"Output of test2: {test2}\n")
test3 = Solution().lengthOfLongestSubstring("pwwkew")
print(f"Output of test3: {test3}")