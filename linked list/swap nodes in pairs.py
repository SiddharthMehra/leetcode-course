# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        prev_node = dummy

        while head and head.next:

            first_node = head
            second_node = head.next

            prev_node.next = second_node #mapping initial dummy node to the second node
            first_node.next = second_node.next # first node next to third node 
            second_node.next = first_node # reversed order of first and second node

            prev_node = first_node
            head = first_node.next
        
        return dummy.next



                
