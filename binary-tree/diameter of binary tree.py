class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        diameter = 0

        def longest_path(node):
            if not node:
                return -1
            
            nonlocal diameter

            left_path = longest_path(node.left)
            right_path = longest_path(node.right)

            diameter = max(diameter, left_path + right_path + 2) # 2 for connecting both to root

            return max(left_path, right_path) + 1 # 1 for connecting node to its parent
        
        longest_path(root)
        return diameter
