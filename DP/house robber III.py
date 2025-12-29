class Solution:
    def rob(self, root):
        memo = {}
        def dp(node, parent_robbed):
            if not node:
                return 0
            
            key = (node, parent_robbed)
            if key in memo:
                return memo[key]
            
            #if parent robbed, you cannot rob the children
            if parent_robbed:
                result = dp(node.left, False) + dp(node.right, False)
            
            else:
                rob = node.val + dp(node.left, True) + dp(node.right, True)
                not_rob = dp(node.left, False) + dp(node.right, False)
                result = max(rob, not_rob)
            
            memo[key] = result
            return result
        
        return dp(root, False)
            
