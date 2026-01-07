class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        MOD = 10**9+7
        n = len(hats)

        #everyone has a hat => done
        done = (1<<n) - 1

        hats_to_people = defaultdict(list)
        for person in range(n):
            for hat in hats[person]:
                hats_to_people[hat].append(person)
        
        memo = {} #(hat, mask)

        def dp(hat, mask):
            if mask == done:
                return 1
            
            if hat>40:
                return 0
            
            if (hat, mask) in memo:
                return memo[(hat, mask)]
            
            #skip the hat
            ans = dp(hat+1, mask)

            #assign this hat to unassigned person
            #(mask | 1<<person sets the person bit, mask & (1<<person) checks if ith bit is set)
            for person in hats_to_people[hat]:
                if mask & (1<<person) == 0:
                    ans = (ans + dp(hat+1, mask | 1<<person)) % MOD
            
            memo[(hat, mask)] = ans
            return ans
        
        return dp(1, 0)


        
