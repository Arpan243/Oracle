from collections import defaultdict
from functools import reduce

def solve(N, from_, to, weight, k):
    # Build adjacency list
    adj = defaultdict(list)
    for i in range(N - 1):
        adj[from_[i]].append((to[i], weight[i]))
        adj[to[i]].append((from_[i], weight[i]))

    def dfs(cur, parent):
        take, skip, diff = [], [], []

        for next_node, w in adj[cur]:
            if next_node != parent:
                not_full, full = dfs(next_node, cur)
                take.append(not_full + w)
                skip.append(full)
                diff.append(take[-1] - skip[-1])

        diff.sort(reverse=True)  # Sort differences in descending order
        ans = [0, 0]

        n = len(diff)
        if n > 0:
            ans[0] = sum(diff[:min(k, n)]) + sum(skip)

            if n >= k:
                ans[1] = ans[0]
                ans[0] -= min(diff[:k])

        return ans

    ans = dfs(0, -1)
    return max(ans[0], ans[1])

# Example usage
N = 5
from_ = [0, 0, 1, 1]
to = [1, 2, 3, 4]
weight = [1, 1, 1, 1]
k = 2

print(solve(N, from_, to, weight, k))  # Example output