class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        curr = [0]*k
        n = len(cookies)

        def dfs(i, zero_count):
            # if not enough cookies to distribute for the remaining children,
            #invalid distribution

            if n-i<zero_count:
                return float('inf')
            
            #unfairness of the distribution after distributing all n cookies
            if i==n:
                return max(curr)
            
            ans = float('inf')
            #distribute ith cookie to jth child
            for j in range(k):
                zero_count-=int(curr[j]==0)
                curr[j]+=cookies[i]

                #update ans as the min unfairness
                ans = min(ans, dfs(i+1, zero_count))

                #roll back the changes 
                curr[j]-=cookies[i]
                zero_count+=int(curr[j]==0)
            
            return ans
        
        return dfs(0, k)
            
