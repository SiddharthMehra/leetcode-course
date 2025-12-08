# design linked list using doubly linked list

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class MyLinkedList:

    def __init__(self):
        #create two dummy nodes left and right, not a part of the linked list
        self.left = ListNode(0)
        self.right = ListNode(0)
        self.left.next = self.right
        self.right.prev = self.left 
        

    def get(self, index: int) -> int:

        curr = self.left.next #first node in the actual linked list
        while curr and index>0:
            curr = curr.next
            index-=1

        if curr and curr!=self.right and index == 0: #you were able to reach a valid index
            return curr.val
        
        return -1
        

    def addAtHead(self, val: int) -> None:

        node, next, prev = ListNode(val), self.left.next, self.left # insert between left and left.next, actual head of the linked list
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev
        

    def addAtTail(self, val: int) -> None:

        node, next, prev = ListNode(val), self.right, self.right.prev #add node after right.prev as right is just a dummy node
        prev.next = node
        next.prev = node
        node.next = next
        node.prev = prev

    def addAtIndex(self, index: int, val: int) -> None:

        curr = self.left.next # actual first node of the linked list

        while curr and index>0:
            curr = curr.next
            index-=1

        if curr and index == 0:
            node, next, prev = ListNode(val), curr, curr.prev # add before curr and after curr.prev
            prev.next = node
            next.prev = node
            node.next = next
            node.prev = prev

    def deleteAtIndex(self, index: int) -> None:

        curr = self.left.next

        while curr and index>0:
            curr = curr.next
            index-=1

        if curr and curr!=self.right and index==0:
            next, prev =  curr.next, curr.prev
            #connect prev and next, delete curr
            next.prev = prev 
            prev.next = next 
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)