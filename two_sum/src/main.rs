use std::vec;

pub struct Solution;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            for j in (i+1)..nums.len() {
                if nums[j] == target - nums[i] {
                    return vec![i as i32,j as i32]
                }
            }
        }
        return vec![]
    }
}

fn main() {
    let first_case = Solution::two_sum(vec![2,7,11,15], 9);
    println!("Indices: {:?}", first_case);
    let second_case = Solution::two_sum(vec![3,2,4], 6);
    println!("Indices: {:?}", second_case);
    let third_case = Solution::two_sum(vec![3,3], 6);
    println!("Indices: {:?}", third_case);
}