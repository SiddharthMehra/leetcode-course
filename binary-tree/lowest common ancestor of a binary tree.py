"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Node:
    def __init__(self, val):
        self.val=val
        self.left=None
        self.right=None
        self.parent=None
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p1, p2 = p, q
        #let's say p1 to root is d1, p2 to root is d2. here, we ensure both distances travel d1+d2 and meet at LCA
        while p1!=p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        
        return p1
