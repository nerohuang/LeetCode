class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0;
        for i in range(len(points) - 1):
            x = points[i + 1][0] - points[i][0];
            y = points[i + 1][1] - points[i][1];
            ans += max(abs(x), abs(y));
        return ans;