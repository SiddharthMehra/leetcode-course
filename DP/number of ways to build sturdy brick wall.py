class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        mod = 10**9+7

        patterns = []

        def generate(pos, cracks):
            if pos == width:
                patterns.append(tuple(cracks))
                return
            
            for b in bricks:
                if pos+b<=width:
                    #add crack if not at end
                    if pos + b<width:
                        generate(pos + b, cracks + [pos+b])
                    
                    else:
                        generate(pos + b, cracks)
            
        generate(0, [])

        pattern_set = [set(p) for p in patterns]

        #build compatability graph
        n = len(patterns)
        compatible = [[] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if pattern_set[i].isdisjoint(pattern_set[j]):
                    compatible[i].append(j)
        
        dp = [[-1] * n for _ in range(height)]

        def solve(row, prev):
            if row == height:
                return 1
            
            if dp[row][prev]!=-1:
                return dp[row][prev]
            
            total = 0
            for nxt in compatible[prev]:
                total = (total + solve(row+1, nxt)) % mod
            
            dp[row][prev] = total
            return total
        
        #start from first row
        result = 0
        for i in range(n):
            result = (result + solve(1, i)) % mod
        
        return result

