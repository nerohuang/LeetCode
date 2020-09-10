class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ans = 0;
        m = len(grid);
        n = len(grid[0]);
        colStore = [];
        rowStore = [];
        for line in grid:
            rowStore.append(line.count(1));
        rotation = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid[0]))] 
        for line in rotation:
            colStore.append(line.count(1));
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if rowStore[i] > 1 or colStore[j] > 1:
                        ans += 1;
        
        return ans
#思路：先计算每行每列有几个机器，然后遍历，遍历到一个机器时就看那个机器的那行那列
#有没有多于1个机器，有就把那个机器计入。

#class Solution:
#    def countServers(self, grid: List[List[int]]) -> int:
#        row, col = collections.defaultdict(set), collections.defaultdict(set)
#        for i, r in enumerate(grid):
#            for j, x in enumerate(r):
#                if x:
#                    row[i].add((i, j))
#                    col[j].add((i, j))
#        ans = set()
#        for v in row.values():
#            if len(v) >= 2:
#                ans |= v
#        for v in col.values():
#            if len(v) >= 2:
#                ans |= v
#        return len(ans)
