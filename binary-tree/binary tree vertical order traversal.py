# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        columnMap = defaultdict(list)
        q = deque([(root, 0)])

        #if node has column col, node.left has column col-1, node.right has col+1
        while q:
            node, col = q.popleft()
            if node is not None:
                columnMap[col].append(node.val)

                q.append((node.left, col-1))
                q.append((node.right, col+1))
        
        #return nodes mapped by columns from left to right in increasing order
        return [columnMap[x] for x in sorted(columnMap.keys())]
        
