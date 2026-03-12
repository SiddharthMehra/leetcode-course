# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        inorder = []
        self.inorder_traversal(root, inorder)

        return self.create_balanced_bst(inorder, 0, len(inorder)-1)
    
    def inorder_traversal(self, root, inorder):
        if not root:
            return
        
        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)
    
    def create_balanced_bst(self, inorder, start, end):
        if start>end:
            return None
        
        mid = (start + end)//2

        left_subtree = self.create_balanced_bst(inorder, start, mid-1)
        right_subtree = self.create_balanced_bst(inorder, mid+1, end)

        node = TreeNode(inorder[mid], left_subtree, right_subtree)
        return node
