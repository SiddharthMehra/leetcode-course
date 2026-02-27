# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def __init__(self):
        self.matchingSubtreeCount = 0
    def calculateSubtreeValues(self, currentNode):
        if currentNode is None:
            return 0, 0
        
        leftSubtree = self.calculateSubtreeValues(currentNode.left)
        rightSubtree = self.calculateSubtreeValues(currentNode.right)

        #calculate the sum of values and number of nodes in current subtree
        sumOfValues = leftSubtree[0] + rightSubtree[0] + currentNode.val
        numberOfNodes = leftSubtree[1] + rightSubtree[1] + 1

        if sumOfValues//numberOfNodes == currentNode.val:
            self.matchingSubtreeCount+=1
        
        return sumOfValues, numberOfNodes

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        self.calculateSubtreeValues(root)
        return self.matchingSubtreeCount
