# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head
        # advance fast to nth position
        for _ in range(n):
            fast = fast.next
        
        if not fast:
            return head.next
        # then advance both fast and slow now they are nth positions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next
        #delete the node
        slow.next = slow.next.next
        return head

# Helper function to convert a standard array into a linked list
def build_linked_list(arr: list) -> Optional[ListNode]:
    if not arr:
        return None
    # Use a dummy node to simplify the initialization loop and avoid special edge cases for the first element.
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        # Instantiate actual ListNode objects to satisfy the algorithm's structural requirements.
        current.next = ListNode(val)
        current = current.next
    # Return the actual head of the newly constructed linked list, skipping the dummy.
    return dummy.next

# Helper function to convert the linked list back to an array for easy console verification
def print_linked_list(head: Optional[ListNode]) -> list:
    # Extract values into a contiguous array to avoid printing raw memory addresses.
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result
    
    
test1 = Solution().removeNthFromEnd(build_linked_list([1,2,3,4,5]), 2)
print(f"Output of test1: {print_linked_list(test1)}\n")
test2 = Solution().removeNthFromEnd(build_linked_list([1]), 1)
print(f"Output of test2: {print_linked_list(test2)}\n")
test3 = Solution().removeNthFromEnd(build_linked_list([1,2]), 1)
print(f"Output of test3: {print_linked_list(test3)}\n")