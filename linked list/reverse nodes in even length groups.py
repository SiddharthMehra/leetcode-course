# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        group_size = 1
        prev_group_end = None

        while curr:
            count = 0 
            temp = curr
            while temp and count<group_size:
                temp = temp.next
                count+=1
            
            #if group size odd skip it
            if count%2==1:
                prev_group_end = curr
                for _ in range(count-1):
                    prev_group_end = prev_group_end.next
                
                curr = temp # set current to next node after group
            
            else:
                #reverse count nodes
                prev = temp
                node = curr
                for _ in range(count):
                    nxt = node.next
                    node.next = prev
                    prev = node
                    node = nxt
                
                if prev_group_end:
                    prev_group_end.next = prev
                else:
                    head = prev
                
                prev_group_end = curr # curr is the new tail
                curr = temp
            
            group_size+=1
        
        return head
                    

        