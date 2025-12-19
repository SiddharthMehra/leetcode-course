#counting sort
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        cnt, remaining = Counter(count.values()), len(count)

        for key in range(1, len(arr)+1):
            if k>=key*cnt[key]:
                k-=key*cnt[key]
                remaining-=cnt[key]
            else:
                return remaining - k // key
        
        return remaining 




    
