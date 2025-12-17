class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(left, right, pivot_index):
            pivot_frequency = count[unique[pivot_index]]

            #move the pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]

            store_index = left
            for i in range(left, right):
                if count[unique[i]]<pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index+=1

            #move pivot to final place
            unique[right], unique[store_index] = unique[store_index], unique[right]

            return store_index
        
        def quickselect(left, right, ksmallest):

            #list contains only one element
            if left == right:
                return
            
            pivot_index = random.randint(left, right)
            pivot_index = partition(left, right, pivot_index)

            if ksmallest == pivot_index:
                return
            
            elif ksmallest<pivot_index:
                quickselect(left, pivot_index-1, ksmallest)
            else:
                quickselect(pivot_index+1, right, ksmallest)
        
        n = len(unique)
        quickselect(0, n-1, n-k)
        return unique[n-k:]
            
