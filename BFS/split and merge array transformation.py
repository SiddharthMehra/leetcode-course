class Solution:
    def minSplitMerge(self, nums1, nums2):

        q = deque()
        n = len(nums1)
        q.append((nums1, 0))
        visit = set()

        while q:
            ne, steps = q.popleft()
            ne = list(ne)

            if ne == nums2:
                return steps
            
            for i in range(n):
                for j in range(i+1, n):
                    x = ne[i:j]
                    temp = ne[:i] + ne[j:]
                    for k in range(n):
                        newl = tuple(temp[:k] + x + temp[k:])
                        if newl not in visit:
                            visit.add(newl)
                            q.append((newl, steps+1))
            
