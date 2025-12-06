class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        prev1 = dummy
        for _ in range(k-1):
            prev1 = prev1.next
        node1 = prev1.next

        prev2 = dummy
        fast = node1 #fast is at node1 k distance away from dummy
        while fast.next:
            fast = fast.next
            prev2 = prev2.next

        node2 = prev2.next

        prev1.next, prev2.next = node2, node1
        node1.next, node2.next = node2.next, node1.next

        return dummy.next