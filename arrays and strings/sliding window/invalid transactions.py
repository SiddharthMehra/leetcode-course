class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        parsed = []
        for t in transactions:
            name, time, amount, city = t.split(',')
            parsed.append((name, int(time), int(amount), city, t))
        
        by_name = defaultdict(list)
        for i, t in enumerate(parsed):
            by_name[t[0]].append(i)
        
        invalid = set()

        #rule 1 -> invalid amount>1000
        for i, (_, _, amount, _, _) in enumerate(parsed):
            if amount>1000:
                invalid.add(i)
        
        #rule2 -> same name, different city, within 60 minutes

        for name, indices in by_name.items():
            indices.sort(key = lambda i: parsed[i][1]) #sorted by time

            window = deque()

            for idx in indices:
                time, city = parsed[idx][1], parsed[idx][3]

                #sliding window of 60 mins
                while window and time - parsed[window[0]][1]>60:
                    window.popleft()
                
                #check conflict, same name different city
                for w in window:
                    if parsed[w][3]!=city:
                        invalid.add(w)
                        invalid.add(idx)
                    
                window.append(idx)
            
        return [parsed[i][4] for i in invalid]
                

        

        
