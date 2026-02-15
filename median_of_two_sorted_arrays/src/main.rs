pub struct Solution;

impl Solution {
    pub fn find_median_sorted_arrays(nums1: Vec<i32>, nums2: Vec<i32>) -> f64 {
        // Ensure nums1 is the smaller array to optimize binary search complexity to O(log(min(m, n)))
        if nums1.len() > nums2.len() {
            return Self::find_median_sorted_arrays(nums2, nums1);
        }

        let (m, n) = (nums1.len(), nums2.len());
        let (mut low, mut high) = (0, m);
        let half_len = (m + n + 1) / 2;

        while low <= high {
            let i = (low + high) / 2; // Partition index for nums1
            let j = half_len - i;     // Partition index for nums2

            // Check if i is too small (nums1[i] < nums2[j-1])
            if i < m && nums2[j - 1] > nums1[i] {
                low = i + 1;
            } 
            // Check if i is too big (nums1[i-1] > nums2[j])
            else if i > 0 && nums1[i - 1] > nums2[j] {
                high = i - 1;
            } 
            // Partition is perfect
            else {
                let max_of_left = if i == 0 {
                    nums2[j - 1] as f64
                } else if j == 0 {
                    nums1[i - 1] as f64
                } else {
                    (nums1[i - 1].max(nums2[j - 1])) as f64
                };

                if (m + n) % 2 == 1 {
                    return max_of_left;
                }

                let min_of_right = if i == m {
                    nums2[j] as f64
                } else if j == n {
                    nums1[i] as f64
                } else {
                    (nums1[i].min(nums2[j])) as f64
                };

                return (max_of_left + min_of_right) / 2.0;
            }
        }
        0.0
    }
}

fn main() {
    let first_case = Solution::find_median_sorted_arrays(vec![1,3], vec![2]);
    println!("First case is {}", first_case);
    let second_case = Solution::find_median_sorted_arrays(vec![1,2], vec![3,4]);
    println!("Second case is {}", second_case);
}
