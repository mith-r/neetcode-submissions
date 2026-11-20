# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        curr = head

        while curr:
            
            #store next
            store = curr.next

            #break link and reattach
            curr.next = prev

            #move prev and head

            prev = curr
            curr = store
        
        return prev



        