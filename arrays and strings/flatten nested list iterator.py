class NestedIterator:

    def __init__(self, nestedList):
        self.generator = self.int_generator(nestedList)
        self.peeked = None
    
    def int_generator(self, nested_list):
        for nested in nested_list:
            if nested.isInteger():
                yield nested.getInteger()
            
            else:
                yield from self.int_generator(nested.getList())
        
    def next(self):
        if not self.hasNext():
            return None
        
        next_integer, self.peeked = self.peeked, None
        return next_integer
    
    def hasNext(self):
        if self.peeked is not None:
            return True
        
        try:
            self.peeked = next(self.generator)
            return True
        except:
            return False
