class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses_count = defaultdict(int)

        for winner, loser in matches:
            losses_count[loser]+=1
            if winner not in losses_count:
                losses_count[winner]=0
        
        ans = [[], []]

        for player, count in losses_count.items():
            if  count==0:
                ans[0].append(player)
            
            elif count==1:
                ans[1].append(player)
        
        return [sorted(ans[0]), sorted(ans[1])]