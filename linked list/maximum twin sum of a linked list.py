# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head
        maximumSum = 0

        #get middle of linked list
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        #reverse second half of linked list
        curr, prev = slow, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        start = head
        while prev:
            maximumSum = max(maximumSum, start.val + prev.val)
            prev = prev.next
            start = start.next
        
        return maximumSum
        
            