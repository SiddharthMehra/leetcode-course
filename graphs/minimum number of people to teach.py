class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:

        user_languages = [set(lang) for lang in languages]
        need_fix = set()

        #find friendships that cannot communicate

        for u,v in friendships:
            u-=1
            v-=1
            if user_languages[u].isdisjoint(user_languages[v]):
                need_fix.add(u)
                need_fix.add(v)
            
        if not need_fix:
            return 0
        
        result = float('inf')

        #try each language
        for lang in range(1, n+1):
            teach_count = 0

            for user in need_fix:
                if lang not in user_languages[user]:
                    teach_count+=1
            
            result = min(result, teach_count)
        
        return result
        
