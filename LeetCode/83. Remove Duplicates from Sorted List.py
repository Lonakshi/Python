
#83. Remove Duplicates from Sorted List

#Given a sorted linked list, delete all duplicates such that each element appear only once.


#code:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        if head is None or head.next is None: return head
        fp = head
        
        while fp.next is not None:
            if fp.val == fp.next.val:
                fp.next = fp.next.next
            else:
                fp= fp.next
        return head
        
