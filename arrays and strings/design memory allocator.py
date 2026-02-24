class Allocator:

    def __init__(self, n):
        self.blocks = [-1] * n
        self.n = n
    
    def allocate(self, size, mID):
        available = 0
        for i in range(self.n):
            if self.blocks[i] == -1:
                available+=1
            
            else:
                available = 0
            
            if available == size:
                for j in range(i - available+1, i+1):
                    self.blocks[j] = mID
                
                return i - available + 1
        
        return -1
    
    def freeMemory(self, mID):
        count = 0
        for i in range(self.n):
            if self.blocks[i] == mID:
                count+=1
                self.blocks[i]=-1
        
        return count


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
