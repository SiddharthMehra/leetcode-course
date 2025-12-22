class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        p1, p2 = 0, 0

        while p1<len(nums1) and p2<len(nums2):
            #only way is to decrease nums[p1]
            if nums1[p1]>nums2[p2]:
                p1+=1
            
            #get distance and move to a smaller p2
            else:
                ans = max(ans, p2 - p1)
                p2+=1
        
        return ans

