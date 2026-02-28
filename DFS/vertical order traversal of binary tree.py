# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []
        
        columnTable = defaultdict(list)
        min_column = max_column = 0

        def dfs(node, row, col):
            if node is not None:
                nonlocal min_column, max_column
                columnTable[col].append((row, node.val))

                min_column = min(min_column, col)
                max_column = max(max_column, col)

                dfs(node.left, row+1, col-1)
                dfs(node.right, row+1, col+1)
        
        dfs(root, 0, 0)

        result = []
        for col in range(min_column, max_column+1):

            result.append([val for row, val in sorted(columnTable[col])])
        
        return result
                
