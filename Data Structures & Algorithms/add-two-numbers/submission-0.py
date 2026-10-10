# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        sum1 = []
        sum2 = []

        num1 = ""
        num2 = ""

        while l1:
            sum1.append(str(l1.val))
            l1 = l1.next
    

        while l2:
            sum2.append(str(l2.val))
            l2=l2.next

        for i in range(len(sum1)-1,-1,-1):
            num1 += sum1[i]

        for i in range(len(sum2)-1,-1,-1):
            num2 += sum2[i]
        
        num3 = int(num1) + int(num2)

        num3 = str(num3)

        print(num3)
        
        res = ListNode(int(num3[-1]))
        curr = res
        
        for i in range(len(num3)-2,-1,-1):
            curr.next = ListNode(int(num3[i]))
            curr = curr.next

        return res