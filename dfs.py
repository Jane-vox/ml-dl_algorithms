'''
第一行，一个正整数 n 表示树中节点个数，k 表示不超过树根的距离，
接下来n−1 行，每行输入两个整数 u, v, 表示节点 u,v之间有一条边。
'''


def dfs(u, fa):
    global ans
    # 如果1号点到u+1点的距离 <= k，则答案加1
    if dist[u] <= k:
        ans += 1
    # 如果1号点到叶子的距离 < k，则还可以再这个叶子下加 k - dist[u] 个
    if u != 0 and len(g[u]) == 1 and dist[u] < k:
        ans += k-dist[u]
        # 继续遍历子树 v
    for v in g[u]:
        if v == fa:
            continue
        dist[v] = dist[u] + 1
        dfs(v, u)

n, k = map(int, input().split())

g = [[] for _ in range(n)]
for _ in range(1, n):  # 行数，有多少条边
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    g[u].append(v)
    g[v].append(u)

INF = int(1e9)
ans = 0
dist = [INF] * n   # 1号点（根节点）到每个点的距离
dist[0] = 0
dfs(0, -1)
print(ans)