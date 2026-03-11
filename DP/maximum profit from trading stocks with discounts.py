from collections import defaultdict
import math

class Solution:
    def maxProfit(self, n, present, future, hierarchy, budget):
        tree = defaultdict(list)
        
        for u, v in hierarchy:
            tree[u-1].append(v-1)

        memo = {}

        def dfs(u, parentBought):
            if (u, parentBought) in memo:
                return memo[(u, parentBought)]

            # cost if we buy this stock
            if parentBought:
                cost = present[u] // 2
            else:
                cost = present[u]

            profit = future[u] - cost

            # case 1: don't buy u
            dp_not = [0] + [-math.inf] * budget

            for v in tree[u]:
                child = dfs(v, 0)
                new = [-math.inf] * (budget + 1)

                for i in range(budget + 1):
                    if dp_not[i] == -math.inf:
                        continue
                    for j in range(budget - i + 1):
                        if child[j] == -math.inf:
                            continue
                        new[i+j] = max(new[i+j], dp_not[i] + child[j])

                dp_not = new

            # case 2: buy u
            dp_buy = [0] + [-math.inf] * budget

            for v in tree[u]:
                child = dfs(v, 1)
                new = [-math.inf] * (budget + 1)

                for i in range(budget + 1):
                    if dp_buy[i] == -math.inf:
                        continue
                    for j in range(budget - i + 1):
                        if child[j] == -math.inf:
                            continue
                        new[i+j] = max(new[i+j], dp_buy[i] + child[j])

                dp_buy = new

            # add u's cost and profit
            final_buy = [-math.inf] * (budget + 1)
            for b in range(budget + 1):
                if dp_buy[b] == -math.inf:
                    continue
                if b + cost <= budget:
                    final_buy[b + cost] = max(final_buy[b + cost], dp_buy[b] + profit)

            # take best of buy or not buy
            res = [max(dp_not[i], final_buy[i]) for i in range(budget + 1)]

            memo[(u, parentBought)] = res
            return res

        ans = dfs(0, 0)
        return max(ans)
