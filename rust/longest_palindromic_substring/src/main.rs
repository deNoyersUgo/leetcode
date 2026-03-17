pub struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        // Edge case: Empty or single char strings are already palindromes.
        if s.len() <= 1 {
            return s;
        }

        let bytes = s.as_bytes();
        let len = bytes.len();
        
        let (mut start, mut max_len) = (0, 0);

        for i in 0..len {
            let len1 = expand_around_center(bytes, i as i32, i as i32);
            
            let len2 = expand_around_center(bytes, i as i32, (i + 1) as i32);
            
            let current_len = std::cmp::max(len1, len2);

            if current_len > max_len {
                max_len = current_len;
                start = i - (current_len - 1) / 2;
            }
        }

        // Return the substring slice converted to a String
        s[start..start + max_len].to_string()
    }
}

// Helper function to expand pointers outward
// Uses i32 to easily handle the 'left < 0' boundary check without usize underflow
fn expand_around_center(s: &[u8], mut left: i32, mut right: i32) -> usize {
    while left >= 0 && (right as usize) < s.len() && s[left as usize] == s[right as usize] {
        left -= 1;
        right += 1;
    }
    (right - left - 1) as usize
}

fn main() {
    let first_case = Solution::longest_palindrome(String::from("babad"));
    println!("First case is {}", first_case);
    let second_case = Solution::longest_palindrome(String::from("cbbd"));
    println!("Second case is {}", second_case);
}
