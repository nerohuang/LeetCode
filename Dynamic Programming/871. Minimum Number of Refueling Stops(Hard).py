class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)

        for i, d in enumerate(dp):
            if d >= target: return i
        return -1

# 思路：
# 这题有两个思路：
# 一个dp，一个heap
# 先说dp
# dp因为不能计数，所以其实就是要看每一个站点最远能到达的距离
# 建立一个dp数组，dp[i]表示第i次加油最远能达到的距离
# 然后只要寻找第一个次距离大于目标距离的位置即可
# 然后每遍历到一个站点的时候，从他为起点倒过来追踪
# 当遍历到的dp[i]大于当前站点的距离，那么就可以判断他
# 下一个站点最远能到哪
# dp[i+1] = max(dp[i+1], dp[i] + capacity)
# 都遍历完成之后
# 就看看谁最先能超越那个距离就可以了
