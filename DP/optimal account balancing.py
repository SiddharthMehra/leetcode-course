#DP +  bitmasking
class Solution:
    def minTransfers(self, transactions: List[List[int]]) -> int:

        balance = defaultdict(int)

        for sender, receiver, amount in transactions:
            balance[sender]-=amount
            balance[receiver]+=amount
        
        #only non zero balances need transfers
        balances = [amt for amt in balance.values() if amt!=0]
        n = len(balances)

        #memo[mask] stores the max number of zero_sum groups in the subset

        memo = [-1] * (1<< n)
        memo[0] = 0

        def dfs(mask):
            if memo[mask]!=-1:
                return memo[mask]
            
            total_sum, max_groups = 0, 0

            #try removing one person at a time
            for i in range(n):
                bit = 1<<i
                if mask & bit: #if person i is in the subset
                    total_sum+=balances[i]
                    remaining_mask = mask ^ bit #remove person i
                    max_groups = max(max_groups, dfs(remaining_mask))
            
            #if total sum of subset is 0, it can form a zero sum group
            memo[mask] = max_groups + (total_sum == 0)
            return memo[mask]
        
        full_mask = (1<<n) - 1
        max_zero_sum_groups = dfs(full_mask)

        #minimum transactions = total people - number of zero sum groups
        return n - max_zero_sum_groups







        
