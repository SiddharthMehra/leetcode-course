# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def dfs(node, path, target):
            if not node:
                return False
            
            if node.val == target:
                return True
            
            #go left
            path.append("L")
            if dfs(node.left, path, target):
                return True
            
            path.pop()

            #go right
            path.append("R")
            if dfs(node.right, path, target):
                return True
            path.pop()

            return False
        
        start_path, dest_path = [], []
        dfs(root, start_path, startValue)
        dfs(root, dest_path, destValue)

        #find split point(LCA)
        i=0
        while i<min(len(start_path), len(dest_path)) and start_path[i] == dest_path[i]:
            i+=1
        
        #go up from startValue to LCA 
        return "U" * (len(start_path[i:]))+ "".join(dest_path[i:])
        

