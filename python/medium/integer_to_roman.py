class Solution:
    def intToRoman(self, num: int) -> str:
        # We pre-compute the entire domain of possible Roman numeral segments.
        # Array indexing is an O(1) memory fetch, completely bypassing the CPU cycles 
        # required for while-loops and repeated mathematical subtraction.
        thousands = ["", "M", "MM", "MMM"]
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        # We construct the final string by mathematically isolating each base-10 digit
        # and fetching its corresponding pre-computed string from the lookup tables.
        # String concatenation here is performed exactly once per decimal place.
        return (thousands[num // 1000] + hundreds[(num % 1000) // 100] + tens[(num % 100) // 10] + ones[num % 10])
        
        
test1 = Solution().intToRoman(3749)
print(f"Output of test1: {test1}\n")
test2 = Solution().intToRoman(58)
print(f"Output of test2: {test2}\n")
test3 = Solution().intToRoman(1994)
print(f"Output of test2: {test3}\n")