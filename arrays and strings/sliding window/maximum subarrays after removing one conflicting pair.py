class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [[] for _ in range(n+1)]
        for a,b in conflictingPairs:
            #setting right and left boundaries, if right is the max of (a,b), left>min(a, b)
            right[max(a,b)].append(min(a,b))
        
        ans = 0
        #largest and second largest, if largest is restricted boundary falls back to second largest
        left = [0, 0]
        subarray_gains = [0]*(n+1)
        for r in range(1, n+1):
            for l in right[r]:
                #either no change or l is the largest or l is the second largest
                left = max(left, [l, left[0]], [left[0], l])
            
            #count number of subarrays with updated boundaries, r and left[0]
            ans+= r-left[0]
            #additional gains made when removing left[0] as boundary falls back to left[1]
            subarray_gains[left[0]] +=left[0] - left[1]
        
        return ans + max(subarray_gains)
        
