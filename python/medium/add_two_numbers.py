# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Including 'carry' in the condition handles the edge case of an extra 
        # digit at the end (e.g., 99 + 1 = 100) without needing a secondary 'if' block.
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Isolating the total computation ensures mathematical clarity 
            # and makes porting this logic to strictly typed languages safer.
            total = val1 + val2 + carry
            carry = total // 10
            
            # We explicitly instantiate a new node. This guarantees our function 
            # has no side effects and does not corrupt the memory of the caller's data.
            current.next = ListNode(total % 10)
            current = current.next
            
            # Safely advance the pointers only if they are currently pointing to a valid node.
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy_head.next
        
# --- Helper Functions for Local Testing ---
def build_linked_list(arr: list) -> ListNode:
    # We iterate through the array backwards to build the list from tail to head.
    # This guarantees O(N) time complexity without needing to track a tail pointer.
    head = None
    for val in reversed(arr):
        head = ListNode(val, head)
    return head

def print_linked_list(node: ListNode) -> list:
    # We convert the linked list back into a standard Python array.
    # This is necessary because printing a ListNode directly just returns 
    # its memory address, which is useless for verifying test outputs.
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
        
sol = Solution()

test1 = sol.addTwoNumbers(build_linked_list([2,4,3]), build_linked_list([5,6,4]))
print(f"Output of test1: {print_linked_list(test1)}\n")
test2 = sol.addTwoNumbers(build_linked_list([0]), build_linked_list([0]))
print(f"Output of test2: {print_linked_list(test2)}\n")
test3 = sol.addTwoNumbers(build_linked_list([9,9,9,9,9,9,9]), build_linked_list([9,9,9,9]))
print(f"Output of test3: {print_linked_list(test3)}\n")