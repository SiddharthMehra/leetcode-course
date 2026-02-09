# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = -float("inf")

        def gainFromSubtree(node):
            nonlocal max_path

            if not node:
                return 0
            
            gainFromLeft = max(gainFromSubtree(node.left), 0)
            gainFromRight = max(gainFromSubtree(node.right), 0)

            max_path = max(max_path, gainFromLeft + gainFromRight + node.val)

            return max(gainFromLeft + node.val, gainFromRight + node.val)
        
        gainFromSubtree(root)
        return max_path
