from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
    
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # edge cases: empty list or single nodes
        if head is None or head.next is None:
            return head
        
        # count the total number of nodes in linked list
        current = head
        list_length = 0
        while current:
            list_length += 1
            current = current.next
        
        # Optimize k by taking modulo with list length to avoid unnecessary rotations
        k %= list_length
       
       # case with k = 0 -> no rotation needed
        if k == 0:
            return head
            
        # two pointers approach to find the rotation point
        # Fast pointer is moved k steps ahead
        fast_pointer = head
        slow_pointer = head
        for _ in range(k):
            fast_pointer = fast_pointer.next
            
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
                    
        # new head is the node after slow_pointer
        new_head = slow_pointer.next
        # break link at the rotation point
        slow_pointer.next = None
        # Connect original tail to the original head
        fast_pointer.next = head
                    
        return new_head
        
sol = Solution()
        
test1 = print_linked_list(sol.rotateRight(build_linked_list([1,2,3,4,5]), 2))
print(f"Output of test1: {test1}\n")
test2 = print_linked_list(sol.rotateRight(build_linked_list([0,1,2]), 4))
print(f"Output of test2: {test2}\n")