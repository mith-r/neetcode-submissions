# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:

        heights = defaultdict(list)

        def tree(node):

            if node is None:
                return -1
            
            leftHeight = tree(node.left)
            rightHeight = tree(node.right)

            currHeight = max(leftHeight, rightHeight) + 1
            heights[currHeight].append(node.val)

            return currHeight        
        
        tree(root)
        
        return list(heights.values())
        