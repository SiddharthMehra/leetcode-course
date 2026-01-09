class RandomizedSet():

    def __init__(self):
        self.dict = {}
        self.list = []
    
    def insert(self, val:int):

        #already inserted
        if val in self.dict:
            return False
        
        self.dict[val] = len(self.list)
        self.list.append(val)
        return True
        
    
    def remove(self, val:int):

        if val in self.dict:
            #move last element to the place of the element to delete and then pop the last element

            last_element, idx = self.list[-1], self.dict[val]
            self.list[idx] = last_element
            self.dict[last_element] = idx

            self.list.pop()
            del self.dict[val]
            return True
        
        return False
    
    def getRandom(self)->int:

        return random.choice(self.list)


