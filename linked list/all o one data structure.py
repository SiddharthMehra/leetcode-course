class Node:
    def __init__(self, freq):
        self.freq = freq
        self.prev = None
        self.next = None
        self.keys = set()

class AllOne:
    def __init__(self):

        self.head = Node(0) #dummy head
        self.tail = Node(0) #dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {} #map of key to node
    
    def inc(self, key: str) ->None:
        if key in self.map:
            node = self.map[key]
            freq = node.freq
            node.keys.remove(key)
        
            nextNode = node.next
            if nextNode == self.tail or nextNode.freq !=freq+1:
                newNode = Node(freq+1)
                newNode.keys.add(key)
                newNode.prev = node
                newNode.next = nextNode
                node.next = newNode
                nextNode.prev = newNode
                self.map[key] = newNode
            else:
                nextNode.keys.add(key)
                self.map[key] = nextNode
        
            if not node.keys:
                self.removeNode(node)
        else:
            firstNode = self.head.next
            if firstNode == self.tail or firstNode.freq>1:
                newNode = Node(1)
                newNode.keys.add(key)
                newNode.prev = self.head
                newNode.next = firstNode
                self.head.next = newNode
                firstNode.prev = newNode
                self.map[key] = newNode
            else:
                firstNode.keys.add(key)
                self.map[key] = firstNode
    
    def dec(self, key)->None:
        if key not in self.map:
            return #key does not exist
        
        node = self.map[key]
        node.keys.remove(key)
        freq = node.freq

        if freq == 1:
            del self.map[key]
        else:
            prevNode = node.prev

            if prevNode == self.head or prevNode.freq!=freq-1:
                newNode = Node(freq-1)
                newNode.keys.add(key)
                newNode.prev = prevNode
                newNode.next = node
                prevNode.next = newNode
                node.prev = newNode
                self.map[key] = newNode
            else:
                prevNode.keys.add(key)
                self.map[key] = prevNode

        if not node.keys:
            self.removeNode(node)     

    def getMaxKey(self):
        #no keys exist
        if self.tail.prev == self.head:
            return ""

        #return one of the keys from the tail's previous node
        return next(iter(self.tail.prev.keys)) 
    
    def getMinKey(self):
        if self.head.next == self.tail:
            return "" #no keys exist
        
        return next(iter(self.head.next.keys))
    
    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode
