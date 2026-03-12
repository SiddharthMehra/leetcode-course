class Solution:
    def longestBalanced(self, s: str) -> int:

        n = len(s)
        p = [[0,0,0]]
        for c in s:
            p.append(p[-1][:])
            p[-1]["abc".index(c)]+=1
        
        ans = 0
        hashmap = {}
        for i, (a,b,c) in enumerate(p):
            for k in [
                (-1, a-b, a-c),
                (-2, a-b, c),
                (-3, b-c, a),
                (-4, c-a, b),
                (-5, b, c),
                (-6, c, a),
                (-7, a, b)
            ]:
                if not k in hashmap:
                    hashmap[k] = i

                #previous occurence of state to new occurence means a,b,c have same counts
                else:
                    ans = max(ans, i - hashmap[k])
            
        return ans
