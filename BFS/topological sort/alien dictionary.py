class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # adj=defaultdict(set)
        # in_degree=Counter({c:0 for word in words for c in word})

        # for first_word, second_word in zip(words, words[1:]):
        #     for c, d in zip(first_word, second_word):
        #         if c!=d:
        #             if d not in adj[c]:
        #                 adj[c].add(d)
        #                 in_degree[d]+=1
        #             break
        #     else:
        #         if len(second_word)<len(first_word):
        #             return ""
        # output=[]
        # queue=deque([c for c in in_degree if in_degree[c]==0])
        # while queue:
        #     c=queue.popleft()
        #     output.append(c)
        #     for d in adj[c]:
        #         in_degree[d]-=1
        #         if in_degree[d]==0:
        #             queue.append(d)
        
        # if len(output)<len(in_degree):
        #     return ""
        # return "".join(output)

        adj = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        #words in sorted order
        for first_word, second_word in zip(words, words[1:]):
            # topological sort c -> d
            for c,d in zip(first_word, second_word):
                if c!=d:
                    if d not in adj[c]:
                        adj[c].add(d)
                        in_degree[d]+=1
                    #only first diff important
                    break
            else:
                #invalid. eg abc<ab, not possible
                if len(second_word)<len(first_word):
                    return ""
        
        output = []
        #topological sort, store in q which have no dependency
        q = deque([ c for c in in_degree if in_degree[c] == 0])

        while q:
            c = q.popleft()
            output.append(c)
            #one dependency from d removed
            for d in adj[c]:
                in_degree[d]-=1
                if in_degree[d] == 0:
                    q.append(d)
        
        #cycle detection
        if len(output)<len(in_degree):
            return ""
        
        return "".join(output)


                    


