# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []
            
        stack = deque()
        stack.append(root)

        res = []
        

        while len(stack) > 0:
            temp = []
            for i in range(len(stack)):

                curr = stack.popleft()
                temp.append(curr.val)

                if curr.left:
                    stack.append(curr.left)
                
                if curr.right:
                    stack.append(curr.right)
            res.append(temp)
        
        return res

        