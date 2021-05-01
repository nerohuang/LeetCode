import collections

edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
def dfs(source,target):
    if source in seen:
        return False
    seen.add(source)
    if source == target:
        return True
    flag = False
    for nei in graph[source]:
        flag = flag or dfs(nei,target)
    return flag

graph = collections.defaultdict(set)

for u,v in edges:
    seen = set()
    if u in graph and v in graph and dfs(u,v):
        print(u,v)
    graph[u].add(v)
    graph[v].add(u)
# 思路
# 应该是DFS
# 题目是要删除掉形成闭环的edge，那么就找到闭环
# 怎么才算闭环，闭环就是如果一个node在u的子集（subnode的subnode）
# 等于 v， 那么就闭环了。
# 比如：
# 1-2
# | |
# 4-3
# [1,2] [2,3] [3,4] 的时候都不是闭环
# 当[1,4]进入之后，1的sub node是2，2的sub node是3，3的subnode是4
# 这样就和4相等了， 这样就闭环了
# 所以我们要一直往某个node的深处找，所以是dfs
# 然后记录下已经访问过node以免访问两次。
# 如果在寻找当中找到了和son相等的father，那么说明他们闭环了。
# 如果没找到，那么双向记录，说明存在这么一条边。
