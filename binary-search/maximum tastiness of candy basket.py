class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
        ans=0

        def checkPrice(mid):
            candies = 1
            last = 0
            for idx in range(1, len(price)):
                if price[idx] - price[last]>=mid:
                    last = idx
                    candies+=1
                
                if candies>=k:
                    return True
            
            return False
        
        l, r = 1, price[-1]-price[0]

        while l<=r:
            mid = (l+r)//2
            if checkPrice(mid):
                ans = mid
                l = mid+1
            else:
                r = mid-1
        
        return ans

            
        
            
