class Excel:

    def __init__(self, height: int, width: str):

        self.h = height
        self.w = width
        self.values = defaultdict(int) # (r,c) ->value
        self.formulas = {}
        self.dependents = defaultdict(set) #reverse graph
    
    def set(self, row, col, val):
        cell = (row, col)

        #remove old formula if exists
        if cell in self.formulas:
            for dep in self.formulas[cell]:
                self.dependents[dep].remove(cell)
            
            del self.formulas[cell]
        
        self.values[cell] = val
        self.update(cell)
    
    def get(self, row, col):
        return self.values[(row, col)]
    
    def sum(self, row, col, numbers):
        cell = (row, col)

        #remove old formula if exists
        if cell in self.formulas:
            for dep in self.formulas[cell]:
                self.dependents[dep].remove(cell)
        
        formula = defaultdict(int)

        for s in numbers:
            if ':' not in s:
                r = int(s[1:])
                c = s[0]
                formula[(r,c)]+=1
            
            else:
                start, end = s.split(':')
                r1, c1 = int(start[1:]), start[0]
                r2, c2 = int(end[1:]), end[0]

                for r in range(r1, r2+1):
                    for c_ord in range(ord(c1), ord(c2)+1):
                        formula[(r, chr(c_ord))]+=1
                
        self.formulas[cell] = formula

        for dep in formula:
            self.dependents[dep].add(cell)
        
        self.calculate(cell)
        self.update(cell)
        return self.values[cell]
    
    def calculate(self, cell):
        if cell not in self.formulas:
            return self.values[cell]
        
        total = 0

        for dep, count in self.formulas[cell].items():
            total+=self.values[dep] * count
        self.values[cell] = total
        return total
    
    def update(self, cell):
        for dependent in self.dependents[cell]:
            self.calculate(dependent)
            self.update(dependent)
        


# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
