# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists) == 0:
            return None

        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))
        

        if len(heap) == 0:
            return None
        
        curr = heapq.heappop(heap)
        curr_index = curr[1]
        curr_node = curr[2]

        node = curr_node
        if curr_node.next:
            heapq.heappush(heap,(curr_node.next.val,curr_index,curr_node.next))
        
        head = node
        
        while len(heap) > 0:
            curr = heapq.heappop(heap)
            curr_index = curr[1]
            curr_node = curr[2]

            if curr_node.next:
                heapq.heappush(heap,(curr_node.next.val,curr_index,curr_node.next))
            
            node.next = curr_node
            node = node.next
        
        node.next = None
        return head

        