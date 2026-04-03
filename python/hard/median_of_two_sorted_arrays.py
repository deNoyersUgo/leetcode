from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We enforce nums1 as the strictly smaller array via a clean recursive call 
        # to ensure we always perform binary search on the shortest possible space.
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        x, y = len(nums1), len(nums2)
        low, high = 0, x

        while low <= high:
            # We partition x exactly in the middle of our active search space.
            partition_x = (low + high) // 2
            
            # We calculate partition_y mathematically to guarantee the total elements 
            # in the left halves perfectly balance the elements in the right halves.
            partition_y = (x + y + 1) // 2 - partition_x

            # We assign infinity boundaries for out-of-bounds indices to seamlessly 
            # handle edge cases where all elements of one array fall on one side of the median.
            max_left_x = float('-inf') if partition_x == 0 else nums1[partition_x - 1]
            min_right_x = float('inf') if partition_x == x else nums1[partition_x]

            max_left_y = float('-inf') if partition_y == 0 else nums2[partition_y - 1]
            min_right_y = float('inf') if partition_y == y else nums2[partition_y]

            # We verify cross-array boundary conditions to confirm the perfect partition.
            if max_left_x <= min_right_y and max_left_y <= min_right_x:
                if (x + y) % 2 == 0:
                    return (max(max_left_x, max_left_y) + min(min_right_x, min_right_y)) / 2.0
                else:
                    return float(max(max_left_x, max_left_y))
            
            # If x's left max is too large, our theoretical median line in x is too far right.
            elif max_left_x > min_right_y:
                high = partition_x - 1
            # Otherwise, the median line in x is too far left.
            else:
                low = partition_x + 1

        # A mathematically guaranteed return path is necessary for strictly typed systems.
        raise ValueError("Input arrays are not properly sorted.")
    
sol = Solution()    
    
test1 = sol.findMedianSortedArrays([1,3], [2])
print(f"Output of test1: {test1}\n")
test2 = sol.findMedianSortedArrays([1,2], [3,4])
print(f"Output of test2: {test2}\n")