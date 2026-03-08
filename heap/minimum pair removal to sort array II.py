import heapq

class Solution:
    def minimumPairRemoval(self, nums):

        n = len(nums)

        if all(a<b for a,b in pairwise(nums)):
            return 0
        
        removed = [False] * n
        prev_index = [i-1 for i in range(n)]
        next_index = [i+1 if (i+1)<n else -1 for i in range(n)]

        #min heap storing (pair_sum, left_index)
        min_heap = [(nums[i] + nums[i+1], i) for i in range(n-1)]
        heapq.heapify(min_heap)

        violation_count = sum(nums[i]>nums[i+1] for i in range(n-1))

        operations = 0
        while violation_count>0:
            pair_sum, left = heapq.heappop(min_heap)

            if removed[left] or next_index[left]==-1:
                continue
            
            right = next_index[left]

            if removed[right] or nums[left] + nums[right]!=pair_sum:
                continue
            
            prev_node = prev_index[left]
            next_node = next_index[right]

            #remove old violations
            if prev_node!=-1 and nums[prev_node]>nums[left]:
                violation_count-=1
            
            if nums[left]>nums[right]:
                violation_count-=1
            
            if next_node!=-1 and nums[right]>nums[next_node]:
                violation_count-=1
            
            nums[left] = pair_sum
            removed[right] = True

            next_index[left] = next_node
            if next_node!=-1:
                prev_index[next_node] = left
            
            #add new violations
            if prev_node!=-1 and nums[prev_node]>nums[left]:
                violation_count+=1
            
            if next_node!=-1 and nums[left]>nums[next_node]:
                violation_count+=1
            
            #push new adjacent numbers to heap
            if prev_node!=-1:
                heapq.heappush(min_heap, (nums[prev_node] + nums[left], prev_node))
            
            if next_node!=-1:
                heapq.heappush(min_heap, (nums[left] + nums[next_node], left))
            
            operations+=1
        
        return operations
