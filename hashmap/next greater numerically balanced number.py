class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x):
            count = Counter(str(x))
            for d, c in count.items():
                if int(d)!=c:
                    return False
            
            return True
        
        x = n+1
        while True:
            if is_balanced(x):
                return x
            x+=1
        
