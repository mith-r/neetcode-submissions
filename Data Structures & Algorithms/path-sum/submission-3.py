# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:\
        # base case, should start popping shit back up
        if root == None:
            return False

        if not (root.left or root.right):
            if root.val == targetSum:
                return True
            else:
                return False
        
        left = False
        right = False
        if root.left:
            left = self.hasPathSum(root.left,targetSum - root.val)

        if root.right:
            right = self.hasPathSum(root.right, targetSum - root.val)
        
        
        return left or right
        
    

        