class Node:
    def __init__(self):
        self.children = {}
        self.content = ""
        self.is_file = False
    

class FileSystem:
    
    def __init__(self):
        self.root = Node()
    
    def ls(self, path):
        node = self.traverse(path)
        if node.is_file:
            return [path.split("/")[-1]]
        
        return sorted(node.children.keys())
    
    def mkdir(self, path):
        self.traverse(path, create = True)
    
    def addContentToFile(self, filePath, content):
        node = self.traverse(filePath, create = True)
        node.is_file = True
        node.content+=content
    
    def readContentFromFile(self, filePath):
        node = self.traverse(filePath)
        return node.content
    
    def traverse(self, path, create: bool = False):
        curr = self.root
        if path == "/":
            return curr
        
        parts = path.split("/")[1:]
        for p in parts:
            if p not in curr.children:
                if not create:
                    return None
                
                curr.children[p] = Node()
            
            curr = curr.children[p]
        
        return curr
    
