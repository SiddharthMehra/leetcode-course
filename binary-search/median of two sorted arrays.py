class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1)>len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low<=high:
            i = (low+high)//2
            j = (m+n+1)//2 - i

            leftA = nums1[i-1] if i>0 else float('-inf')
            rightA = nums1[i] if i<m else float('inf')
            leftB = nums2[j-1] if j>0 else float('-inf')
            rightB = nums2[j] if j<n else float('inf')

            if leftA<=rightB and leftB<=rightA:

                if (m+n) % 2==0:
                    return (max(leftA, leftB) + min(rightA, rightB))/2
                else:
                    return max(leftA, leftB)
                
            elif leftA>rightB:
                high = i-1
            else:
                low = i+1
            



