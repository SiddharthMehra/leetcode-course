class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        #sort in order and fetch the top 3 results
        products.sort()
        curr, ans = '', []
        for char in searchWord:
            curr+=char
            i = bisect.bisect_left(products, curr)
            ans.append([product for product in products[i:i+3] if product.startswith(curr)])
    
        return ans

            



