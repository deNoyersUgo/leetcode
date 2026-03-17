// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

fn internal_add_two_number(
    l1: &Option<Box<ListNode>>,
    l2: &Option<Box<ListNode>>,
    carry: i32,
) -> Option<Box<ListNode>> {
    // Why Match?
    // We match on the tuple (l1, l2) to explicitly visualize the state matrix.
    // This removes the mutable state variables ('sum', 'l1', 'l2') entirely,
    // making the function purely functional and easier to reason about mathematically.
    match (l1, l2) {
        (None, None) => {
            if carry > 0 {
                Some(Box::new(ListNode::new(carry)))
            } else {
                None
            }
        }
        // Case: Only one list has nodes left (handles both l1 or l2 being Some)
        (Some(node), None) | (None, Some(node)) => {
            let sum = node.val + carry;
            Some(Box::new(ListNode {
                val: sum % 10,
                // Recurse: We pass 'None' explicitly for the empty side to keep logic uniform
                next: internal_add_two_number(&node.next, &None, sum / 10),
            }))
        }
        // Case: Both lists have nodes
        (Some(n1), Some(n2)) => {
            let sum = n1.val + n2.val + carry;
            Some(Box::new(ListNode {
                val: sum % 10,
                next: internal_add_two_number(&n1.next, &n2.next, sum / 10),
            }))
        }
    }
}

pub struct Solution;

impl Solution {
    pub fn add_two_numbers(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        internal_add_two_number(&l1, &l2, 0)
    }
}

fn main() {
    fn to_list(nums: &[i32]) -> Option<Box<ListNode>> {
        let mut head = None;
        for &x in nums.iter().rev() {
            let mut node = ListNode::new(x);
            node.next = head;
            head = Some(Box::new(node));
        }
        head
    }

    let first_case = Solution::add_two_numbers(to_list(&[2, 4, 3]), to_list(&[5, 6, 4]));
    println!("Result 1: {:?}", first_case);

    let second_case = Solution::add_two_numbers(to_list(&[0]), to_list(&[0]));
    println!("Result 2: {:?}", second_case);

    let third_case = Solution::add_two_numbers(to_list(&[9, 9, 9, 9, 9, 9, 9]), to_list(&[9, 9, 9, 9]));
    println!("Result 3: {:?}", third_case);
}