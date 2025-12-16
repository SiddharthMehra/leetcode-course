# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        q = deque([root])
        level = 0

        while q:
            prevVal = None

            for _ in range(len(q)):
                node = q.popleft()

                #check even odd conditions
                if (level%2==0 and (node.val%2 == 0 or (prevVal is not None and node.val<=prevVal))) or \
                (level%2==1 and (node.val%2==1 or (prevVal is not None and node.val>=prevVal))):
                    return False
                
                prevVal = node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            level+=1

        return True






        
