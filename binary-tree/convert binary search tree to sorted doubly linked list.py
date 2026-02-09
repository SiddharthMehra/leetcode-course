"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':

        def helper(node):

            nonlocal prev, first

            #standard inorder traversal
            if node:
                helper(node.left)

                if prev:
                    prev.right = node
                    node.left = prev
                
                else:
                    first = node
                prev = node

                helper(node.right)

        if not root:
            return None
        
        first, prev = None, None
        helper(root)

        prev.right = first
        first.left = prev
        return first

