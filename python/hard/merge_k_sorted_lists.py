from typing import List, Optional
from heapq import heappop, heappush

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        
        # WHY: We push only the head of each linked list to keep our heap size strictly bounded to O(K).
        # WHY: We use an index 'i' as a tie-breaker so heapq never attempts to compare two ListNode objects directly if their values are equal.
        for i, node in enumerate(lists):
            if node:
                heappush(heap, (node.val, i, node))
        
        # WHY: A dummy node simplifies edge cases so we don't have to handle the initialization of the head pointer separately.
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            # WHY: Extract the smallest current node to attach to our continuous merged list.
            val, i, node = heappop(heap)
            current.next = node
            current = current.next
            
            # WHY: If the extracted node has a subsequent element, push it into the heap to maintain our K active candidates.
            if node.next:
                heappush(heap, (node.next.val, i, node.next))
                
        return dummy.next

# Helper function to convert a list to a linked list
def list_to_linkedlist(items):
    # WHY: The dummy node allows clean, uniform traversal and appending without initial None checks.
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
    # WHY: Returning the items array prevents the f-string from evaluating a print() function's inherently None return type.
    return items

sol = Solution()

# Test cases
# WHY: We use a list comprehension to map the helper function over each individual sub-array, generating the required List[ListNode].
test1_input = [list_to_linkedlist(l) for l in [[1,4,5],[1,3,4],[2,6]]]
test1 = sol.mergeKLists(test1_input)
print(f"Output of test1: {print_linked_list(test1)}\n")

test2 = sol.mergeKLists([])
print(f"Output of test2: {print_linked_list(test2)}\n")

test3_input = [list_to_linkedlist(l) for l in [[]]]
test3 = sol.mergeKLists(test3_input)
print(f"Output of test3: {print_linked_list(test3)}\n")