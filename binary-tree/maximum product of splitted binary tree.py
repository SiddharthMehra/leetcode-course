# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        tree_sums = []

        def dfs(node):
            if not node:
                return 0
            
            l_sum = dfs(node.left)
            r_sum = dfs(node.right)
            curr_sum = l_sum + r_sum + node.val

            tree_sums.append(curr_sum)

            return curr_sum
        
        total_sum = dfs(root)

        max_product = 0

        for sum in tree_sums:
            max_product = max(max_product, sum * (total_sum - sum))
        
        return max_product % (10**9+7)
