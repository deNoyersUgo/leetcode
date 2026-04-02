class Solution:
    def romanToInt(self, s: str) -> int:
        # We define the constant mapping matrix.
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        total = 0
        prev_val = 0
        
        # We iterate backward using a generator (reversed). 
        # This completely avoids index out-of-bounds checks and physical array slicing.
        for char in reversed(s):
            print(f"Char is {char}")
            # We fetch the integer value exactly once per character, 
            # cutting the expensive dictionary lookups in half compared to left-to-right.
            val = roman_to_int[char]
            print(f"Val is {val}")
            print(f"Prev_val is {prev_val}")
            # Since we move right-to-left, if the current value is strictly less 
            # than the right-adjacent value we just processed, it must be subtractive.
            if val < prev_val:
                print(f"Subtracting {val} to {total}")
                total -= val
                print(f"Total is {total}")
            else:
                print(f"Add {val} to {total}")
                total += val
                print(f"Total is {total}")
                # We update our tracking variable to the current value. 
                # This acts as our "look-ahead" state for the next iteration.
                prev_val = val
                
        return total









test1 = Solution().romanToInt("III")
print(f"Output of test1: {test1}\n")
test2 = Solution().romanToInt("LVIII")
print(f"Output of test1: {test2}\n")
test3 = Solution().romanToInt("MCMXCIV")
print(f"Output of test1: {test3}\n")