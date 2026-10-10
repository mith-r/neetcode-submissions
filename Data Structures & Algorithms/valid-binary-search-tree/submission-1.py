# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def tree(node, left, right):

            if not node:
                return True
            
            if not (left<node.val<right):
                return False
            
            return tree(node.left,left,node.val) and tree(node.right,node.val,right)

            
            #base case is if you get to a lea

        return tree(root, float("-inf"), float("inf"))
        