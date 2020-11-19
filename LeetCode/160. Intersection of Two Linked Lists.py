#160. Intersection of Two Linked Lists


#Write a program to find the node at which the intersection of two singly linked lists begins.

#code: # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB: return None
        
        a,b= headA, headB
        
        while a!=b:
            if not a:
                a=headB
            else:
                a=a.next
            
            if not b:
                b= headA
            else:
                b= b.next
        return a
                
        
       
    #a= 4->1->8->4->5
    #b= 5->6->1>8->4->5
    
    #ab = 4->1->8->4->5->5->6->1->8->-4->5
    #ba= 5->6->1->8->4->5->4->1->->8->4->5
   
        
