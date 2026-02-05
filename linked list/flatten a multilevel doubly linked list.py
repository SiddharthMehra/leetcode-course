"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return 
        
        dummy = Node(0, None, head, None)
        prev = dummy

        stack = []
        stack.append(head)

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            #stack is LIFO, add next first, child later processed in reverse order
            if curr.next:
                stack.append(curr.next)
            
            if curr.child:
                stack.append(curr.child)

                curr.child = None
            
            prev = curr
        
        dummy.next.prev = None
        return dummy.next

        
