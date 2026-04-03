from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone_mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz",
        }
        
        combinations = []
        
        def backtrack(index, path):
            #print("Backtrack is called")
            if index == len(digits):
                combinations.append("".join(path))
                #print(f"combinations is now {combinations}")
                return
            
            possible_letters = phone_mapping[digits[index]]
            #print(f"possible_letters is {possible_letters}")
            for letter in possible_letters:
                #print(f"letter is now {letter}")
                path.append(letter)
                #print(f"path is now {path}")
                backtrack(index + 1, path)
                #print("Backtrack has been called and we are about to pop path")
                path.pop()  # Backtrack
                #print(f"path is after pop {path}")
                
        backtrack(0, [])
        return combinations

sol = Solution()

test1 = sol.letterCombinations("23")
print(f"Output of test1: {test1}\n")
test2 = sol.letterCombinations("2")
print(f"Output of test2: {test2}\n")