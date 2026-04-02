class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[ans] = nums[i]
                ans += 1
        return ans
    
test1 = Solution().removeDuplicates([1,1,2])
print(f"Output of test1: {test1}\n")
test2 = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
print(f"Output of test2: {test2}\n")