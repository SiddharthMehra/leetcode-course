# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        dp = {}

        def build(l, r):
            if l>r:
                return [None]
            
            if (l, r) in dp:
                return dp[(l, r)]
            
            res = []
            for root in range(l, r+1):
                leftTree = build(l, root-1)
                rightTree = build(root+1, r)

                for left in leftTree:
                    for right in rightTree:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        res.append(node)
            
            dp[(l, r)] = res
            return res
        
        return build(1, n)
                        
