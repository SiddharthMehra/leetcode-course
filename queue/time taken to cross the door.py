class Solution:
    def timeTaken(self, arrival: List[int], state: List[int]) -> List[int]:

        n = len(arrival)
        enterQ, exitQ = deque(), deque()

        ans = [0] * n
        time = 0
        i = 0
        last_used = -1 #-1 unused, 0 enter, 1 exit

        while i<n or enterQ or exitQ:

            while i<n and arrival[i]<=time:
                if state[i] == 0:
                    enterQ.append(i)
                
                else:
                    exitQ.append(i)
                
                i+=1
            
            if enterQ or exitQ:

                if enterQ and exitQ:
                    if last_used==-1:
                        idx = exitQ.popleft()
                        last_used = 1
                    
                    elif last_used == 0:
                        idx = enterQ.popleft()
                        last_used = 0
                    
                    else:
                        idx = exitQ.popleft()
                        last_used = 1
                    
                elif exitQ:
                    idx = exitQ.popleft()
                    last_used = 1
                
                else:
                    idx = enterQ.popleft()
                    last_used = 0
                
                ans[idx] = time
                time+=1

            else:
                last_used = -1
                time = arrival[i]
            
        
        return ans
