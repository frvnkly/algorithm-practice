# Remove all elements from a linked list of integers that have value val.

# Example:

# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        ptr1 = head
        while ptr1 and ptr1.val == val:
            ptr1 = ptr1.next
        head = ptr1
        
        prev = None
        ptr2 = head
        while ptr2:
            if ptr2.val == val:
                prev.next = ptr2.next
            else:
                prev = ptr2
            ptr2 = ptr2.next
        
        return head
        