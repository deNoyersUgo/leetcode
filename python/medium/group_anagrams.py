from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_groups = defaultdict(list)
        
        for s in strs:
            key = ''.join(sorted(s))
            anagrams_groups[key].append(s)
        
        return list(anagrams_groups.values())
            
sol = Solution()

test1 = sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(f"Output of test1: {test1}\n")
test2 = sol.groupAnagrams([""])
print(f"Output of test2: {test2}\n")
test3 = sol.groupAnagrams(["a"])
print(f"Output of test3: {test3}\n")