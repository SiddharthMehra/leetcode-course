# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#inorder traversal
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        self.minDistance = 1e9

        self.prevNode = None

        def inorder(node):

            if node is None:
                return
            
            inorder(node.left)

            if self.prevNode is not None:
                self.minDistance = min(self.minDistance, node.val - self.prevNode)
            
            self.prevNode = node.val
            inorder(node.right)
        
        inorder(root)
        return self.minDistance

        
