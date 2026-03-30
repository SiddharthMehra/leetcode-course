# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:

        dummy = ListNode(-1, head)
        frequency = defaultdict(int)
        temp = head
        current = dummy.next
        prev = dummy

        #count occurences of each value in the linked list
        while temp:
            frequency[temp.val]+=1
            temp = temp.next
        
        #traverse the list and remove nodes appearing more than once
        while current:
            if frequency[current.val]>1:
                prev.next = current.next
            else:
                prev = current
            
            current = current.next
        
        return dummy.next

        
