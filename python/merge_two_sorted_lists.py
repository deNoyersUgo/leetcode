# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        # Initialize a dummy node to simplify edge cases
        dummy = ListNode()
        current = dummy

        # Pointers for list1 and list2
        p1 = list1
        p2 = list2

        # Traverse both lists
        while p1 and p2:
            if p1.val <= p2.val:
                current.next = p1
                p1 = p1.next
            else:
                current.next = p2
                p2 = p2.next
            current = current.next

        # Attach the remaining nodes
        if p1:
            current.next = p1
        elif p2:
            current.next = p2

        # Return the merged list starting from the next of dummy node
        return dummy.next

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

# Test cases
test1 = Solution().mergeTwoLists(list_to_linkedlist([1,2,4]), list_to_linkedlist([1,3,4]))
print(f"Output of test1: {print_linked_list(test1)}\n")
test2 = Solution().mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([]))
print(f"Output of test2: {print_linked_list(test2)}\n")
test3 = Solution().mergeTwoLists(list_to_linkedlist([]), list_to_linkedlist([0]))
print(f"Output of test3: {print_linked_list(test3)}\n")