class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        out = []
        
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]: 
                continue
            
            left, right = i+1, len(nums) - 1
            
            while left < right:
                threeSum = n + nums[left] + nums[right]
                
                if threeSum < 0:
                    left += 1
                elif threeSum > 0:
                    right -= 1
                else:
                    out.append([n, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
                    
                    while nums[right] == nums[right+1] and left < right:
                        right -= 1           
        return out
                    
sol = Solution()        

test1 = sol.threeSum([-1,0,1,2,-1,-4])
print(f"Output of test1: {test1}\n")
test2 = sol.threeSum([0,1,1])
print(f"Output of test2: {test2}\n")
test3 = sol.threeSum([0,0,0])
print(f"Output of test3: {test3}\n")