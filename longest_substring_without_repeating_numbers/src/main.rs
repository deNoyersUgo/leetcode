pub struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut longest: usize = 0;
        let mut current: Vec<char> = Vec::new();

        for c in s.chars() {
            if let Some(index) = current.iter().position(|&x| x == c) {
                longest = std::cmp::max(current.len(), longest);

                for _ in 0..=index {
                    current.remove(0);
                }
            }

            current.push(c);
        }

        std::cmp::max(current.len(), longest) as i32
    }
}

fn main() {
    let first_case = Solution::length_of_longest_substring(String::from("abcabcbb"));
    println!("First case is {}", first_case);
    let second_case = Solution::length_of_longest_substring(String::from("bbbbb"));
    println!("First case is {}", second_case);
    let third_case = Solution::length_of_longest_substring(String::from("pwwkew"));
    println!("First case is {}", third_case)
}