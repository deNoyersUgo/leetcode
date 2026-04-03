class Solution:
    def countAndSay(self, n: int) -> str:
        res = '1'
        
        for _ in range(1,n):
            prev, count = '.', 0
            curr_str = ""
            
            for char in res:
                if char == prev or prev == '.':
                    count += 1
                else:
                    curr_str += str(count) + prev
                    count = 1
                prev = char
            
            curr_str += str(count) + prev
            res = curr_str
            
        return res
   
sol = Solution()   
        
test1 = sol.countAndSay(1)
print(f"Output of test1: {test1}\n")
test2 = sol.countAndSay(4)
print(f"Output of test2: {test2}\n")