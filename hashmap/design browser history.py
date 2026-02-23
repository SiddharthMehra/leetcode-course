class BrowserHistory:

    def __init__(self, homepage:str):
        self.visited_URLs = [homepage]
        self.curr_URL, self.last_URL = 0, 0
    
    def visit(self, url:str)->None:
        self.curr_URL+=1
        if len(self.visited_URLs)>self.curr_URL:
            self.visited_URLs[self.curr_URL] = url
        
        else:
            self.visited_URLs.append(url)
        
        self.last_URL =  self.curr_URL
    
    def back(self, steps:int)->str:

        self.curr_URL = max(0, self.curr_URL - steps)
        return self.visited_URLs[self.curr_URL]

    def forward(self, steps:int)->str:
        
        self.curr_URL = min(self.last_URL, self.curr_URL + steps)
        return self.visited_URLs[self.curr_URL]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
