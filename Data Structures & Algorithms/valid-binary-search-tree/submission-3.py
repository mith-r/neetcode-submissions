# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
        low = float("-inf")
        high = float("inf")

        def dfs(root,low,high):

            if not root:
                return False
            
            a=True
            b=True

            if root.left:
                a=dfs(root.left,low,root.val)
            
            if root.right:
                b=dfs(root.right,root.val,high)

            return root.val > low and root.val < high and a and b
        
        return dfs(root,low,high)