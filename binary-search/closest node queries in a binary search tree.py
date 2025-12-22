# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        def inorder(node, sorted_values):
            if not node:
                return
            inorder(node.left, sorted_values)
            sorted_values.append(node.val)
            inorder(node.right, sorted_values)
        
        nums = []
        inorder(root, nums)
        results, n = [], len(nums)

        for q in queries:
            i = bisect_left(nums, q)
            if i<n and nums[i] == q: results.append([q,q])
            else:
                if i==0: results.append([-1, nums[0]]) #smallest element in the array
                elif i==n: results.append([nums[-1], -1])#largest element
                else: results.append([nums[i-1], nums[i]])
        
        return results

        
