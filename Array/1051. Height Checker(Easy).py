class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortHeights = heights.copy();
        sortHeights.sort();
        ans = 0;
        for i in range(len(heights)):
            if sortHeights[i] != heights[i]:
                ans += 1;
        return ans;

##class Solution:
##    def heightChecker(self, heights: List[int]) -> int:
##        sortedH = sorted(heights)
##        count = 0
##        for i in range(len(heights)):
##            if heights[i] != sortedH[i]:
##                count += 1
##        return count