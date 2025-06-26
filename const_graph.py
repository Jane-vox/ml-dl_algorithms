
'''
n个点，m条边，每行输入两个整数a，b，表示a->b连接一条有向边
最后一行输入n个整数，表示n个点的点权
4 3
1 2
2 3
3 4
1 2 3 4
'''

N = 100010
g = [[] for _ in range(N)]
w = [0] * N

# dfs
def dfs(u, fa):
    # Do things
    for x in g[u]:
        if x == fa:  # 防止在无向图的遍历中出现重复访问;有向图不需要fa这个参数
            continue
        dfs(x, u)
        # Do things

n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)   # a->b建立一条有向边

w[1:] = map(int, input().split())


'''
n个点，每行输入三个整数a,b,c 表示a--b连接一条边权为c的无向边
4 3
1 2 3
2 3 2
3 4 2
'''
from collections import defaultdict

n = int(input())
g = defaultdict(list)   # 创建的邻接表
f = [0] * (n + 1)  # 长度为 n + 1 的列表，用于存储每个节点的某种属性值

def dfs(u, fa):
    global f
    for x, w in g[u]:
        if x == fa:
            continue
        dfs(x, u)
        #代码逻辑

for _ in range(1, n):
    a, b, c = map(int, input().split())
    g[a].append((b, c))
    g[b].append((a, c))  # 无向边就正反都加一遍


