# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def preorder(node, curr_sum):
            nonlocal count
            if not node:
                return
            
            curr_sum+=node.val

            if curr_sum == k: #found path
                count+=1
            
            count+=h[curr_sum-k]

            h[curr_sum]+=1

            #preorder traversal
            preorder(node.left, curr_sum)
            preorder(node.right, curr_sum)

            #backtrack
            h[curr_sum]-=1
        
        count, k = 0, targetSum
        h = defaultdict(int)
        preorder(root, 0)
        return count



        
