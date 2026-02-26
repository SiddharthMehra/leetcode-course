class Node:

    def __init__(self, char: str="", prev = None, next = None):
        self.char = char
        self.prev, self.next = prev, next
    
class TextEditor:

    def __init__(self):
        self.head, self.tail = Node(), Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        #cursor initially at the beginning
        self.cursor = self.head
    
    def addText(self, text):
        for char in text:
            new_node = Node(char)
            new_node.prev = self.cursor
            new_node.next = self.cursor.next
            self.cursor.next.prev = new_node
            self.cursor.next = new_node
            self.cursor = new_node
    
    def deleteText(self, k):
        count = 0
        while k>0 and self.cursor!=self.head:
            prev_node = self.cursor.prev
            prev_node.next = self.cursor.next
            self.cursor.next.prev = prev_node
            self.cursor = prev_node
            k-=1
            count+=1
        return count
    
    def cursorLeft(self, k):
        while k>0 and self.cursor!=self.head:
            self.cursor = self.cursor.prev
            k-=1
        return self.getLeftText()
    
    def cursorRight(self, k):
        while k>0 and self.cursor.next!=self.tail:
            self.cursor = self.cursor.next
            k-=1
        return self.getLeftText()
    
    def getLeftText(self):
        text = []
        curr = self.cursor
        count = 0
        while curr!=self.head and count<10:
            text.append(curr.char)
            curr = curr.prev
            count+=1
        
        return "".join(text[::-1])
    
