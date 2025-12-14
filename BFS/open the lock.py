class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadEndSet = set(deadends)
        q = deque()
        q.append(('0000', 0))
        visited = set('0000')

        while q:
            curr, steps = q.popleft()
            if curr == target:
                return steps
            
            if curr in deadEndSet:
                continue
            
            for i in range(4):
                digit = int(curr[i])
                for dir in [1,-1]:
                    newDigit = (digit+dir)%10
                    newCurr = curr[:i] + str(newDigit) + curr[i+1:]

                    if newCurr not in visited:
                        visited.add(newCurr)
                        q.append((newCurr, steps+1))
        
        return -1
                    
            

        



        
