#longest path from root to furthest leaf node

class Solution:
    def maxDepth(self, root):

        if root is None:
            return 0
        
        else:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

            return max(left, right)+1




