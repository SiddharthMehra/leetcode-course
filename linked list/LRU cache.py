class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {} #map key to node

        #left and right connector nodes
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
    
    #remove node by connecting prev and next nodes
    def remove(self, node): 
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node):
        
        #adding node after right.prev(actual last node) and before right
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) :
        #left LRU, right most recently used
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        
        return -1


    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache)>self.cap:
            #remove from list and delete lru from hashmap(i.e delete from left)
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


