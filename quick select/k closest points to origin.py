class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(i):
            return points[i][0]**2 + points[i][1]**2
        
        def partition(left, right, pivot_index):
            pivot_dist = dist(pivot_index)
        
            points[pivot_index], points[right] = points[right], points[pivot_index]

            store_index = left
            for i in range(left, right):
                if dist(i)<=pivot_dist:
                    points[i], points[store_index] = points[store_index], points[i]
                    store_index+=1
            
            points[store_index], points[right] = points[right], points[store_index]
            return store_index
        
        def quickselect(left, right):
            if left>=right:
                return
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if pivot_index == k:
                return
            
            elif pivot_index<k:
                quickselect(pivot_index+1, right)
            
            else:
                quickselect(left, pivot_index-1)
        
        quickselect(0, len(points)-1)
        return points[:k]
