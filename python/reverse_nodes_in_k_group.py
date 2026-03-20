# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        tail = head
        
        for _ in range(k):
            if not tail:
                return head
            tail = tail.next
        newHead = self._reverse(head, tail)
        head.next = self.reverseKGroup(tail,k)
        
        return newHead
        
    def _reverse(self, head: Optional[ListNode], tail: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr != tail:
            next = curr.next
            curr.next = prev
            prev = curr
            curr =next
        return prev
        

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
    
    
test1 = Solution().reverseKGroup(list_to_linkedlist([1,2,3,4,5]),2)
print(f"Output of test1: {print_linked_list(test1)}\n")
test2 = Solution().reverseKGroup(list_to_linkedlist([1,2,3,4,5]), 3)
print(f"Output of test2: {print_linked_list(test2)}\n")
