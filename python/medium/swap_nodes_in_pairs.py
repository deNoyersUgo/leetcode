from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        first = head
        second = head.next
    
        # Swapping
        first.next = self.swapPairs(second.next)
        second.next = first
    
        return second

# Helper function to convert a list to a linked list
def list_to_linkedlist(items):
    dummy = ListNode()
    current = dummy
    for item in items:
        current.next = ListNode(val=item)
        current = current.next
    return dummy.next

# Helper function to print a linked list
def print_linked_list(head):
    items = []
    while head:
        items.append(head.val)
        head = head.next
    return items
    
    
test1 = Solution().swapPairs(list_to_linkedlist([1,2,3,4]))
print(f"Output of test1: {print_linked_list(test1)}\n")
test2 = Solution().swapPairs(list_to_linkedlist([]))
print(f"Output of test2: {print_linked_list(test2)}\n")
test3 = Solution().swapPairs(list_to_linkedlist([1]))
print(f"Output of test3: {print_linked_list(test3)}\n")
test4 = Solution().swapPairs(list_to_linkedlist([1,2,3]))
print(f"Output of test4: {print_linked_list(test4)}\n")