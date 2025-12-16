# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #one right and then left
    def successor (self, root):
        root = root.right
        while root.left:
            root = root.left
        return root.val
    
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        
        return root.val
    
    def deleteNode(self, root, key):
        if not root:
            return None
        
        if key>root.val:
            root.right = self.deleteNode(root.right, key)
        
        elif key<root.val:
            root.left = self.deleteNode(root.left, key)
        
        else:
            #node to be deleted is a leaf
            if not ( root.left or root.right):
                root = None
            #replace the node by its successor
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            
            else:
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        
        return root

            

            
        
        
