class Node:

    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode

class MyCircularQueue:

    def __init__(self, k):
        self.capacity = k
        self.head = None
        self.tail = None
        self.count = 0
    
    def enQueue(self, k):
        if self.count == self.capacity:
            return False
        
        #empty, so first element, initially head is the same as tail
        if self.count == 0:
            self.head = Node(k)
            self.tail = self.head
        
        #add at the end
        else:
            newNode = Node(k)
            self.tail.next = newNode
            self.tail = newNode
        
        self.count+=1
        return True

    #delete an element from the left
    def deQueue(self):
        if self.count == 0:
            return False
        
        self.head = self.head.next
        self.count-=1
        return True
    
    #front item of the queue
    def Front(self):
        if self.count == 0:
            return -1
        
        return self.head.value
    
    def Rear(self):

        if self.count == 0:
            return -1
        
        return self.tail.value
    
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count == self.capacity
