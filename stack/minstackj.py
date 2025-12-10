# min stack using two stacks all operations in O(1)

class MinStack:

    def __init__(self):

        self.stack = []
        self.min_stack = []
        
    def push(self, val: int) -> None:

        self.stack.append(x)

        if not self.min_stack or x<self.min_stack[-1][0]:
            self.min_stack.append([x, 1])
        
        elif x == self.min_stack[-1][0]:
            self.min_stack[-1][1]+=1
       

    def pop(self) -> None:

        if self.min_stack[-1][0] == self.stack[-1]:
            self.min_stack[-1][1]-=1
        
        if self.min_stacl[-1][1]==0:
            self.min_stack.pop()
        
        self.stack.pop()


    def top(self) -> int:

        return self.stack[-1]

        

    def getMin(self) -> int:

        return self.min_stack[-1][0]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()