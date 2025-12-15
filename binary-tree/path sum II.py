# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#backtracking
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        res = []
        def dfs(node, path, currSum):
            if not node:
                return
            
            currSum+=node.val
            path.append(node.val)
            if not node.left and not node.right and currSum == targetSum:
                res.append(path[:])
            
            dfs(node.left, path, currSum)
            dfs(node.right, path, currSum)

            path.pop() #backtrack
        
        dfs(root, [], 0)
        return res


        
