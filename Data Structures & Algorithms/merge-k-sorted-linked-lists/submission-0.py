# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode:
    def __init__(self,val=0, next = None):
        self.val = val
        self.next = next
    
    def __lt__ (self,other):
        return self.val < other.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        heap = []

        if len(lists) == 0:
            return None

        for head in lists:

            while head:
                heapq.heappush(heap,(head.val,head))
                head = head.next
        
        if len(heap) == 0:
            return None
        
        head = heapq.heappop(heap)[1]
        node = head

        while len(heap) > 0:
            node.next = heapq.heappop(heap)[1]
            node = node.next

        return head

            

        