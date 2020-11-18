#876. Middle of the Linked List


#Given a non-empty, singly linked list with head node head, return a middle node of linked list.

#If there are two middle nodes, return the second middle node.

 


#code

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow_pointer = head
        fast_pointer = head
        
        if head is not None:
            while(fast_pointer is not None and fast_pointer.next is not None):
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            
            return slow_pointer
      
