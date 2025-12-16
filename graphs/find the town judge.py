class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        if len(trust)<n-1:
            return -1
        
        trust_scores = [0]*(n+1)

        for a,b in trust:
            trust_scores[a]-=1
            trust_scores[b]+=1
        
        for i in range(len(trust_scores)):
            if trust_scores[i]==n-1:
                return i
        
        return -1
