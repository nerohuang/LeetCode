class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0;
        l = 0;
        r = len(height) - 1;
        while l < r:
            result = max(result, min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]):
                l += 1;
            else:
                r -= 1;
        return result;

# 思路 
# 想法很简单，就是一左一右两个pointer
# 然后每次用max来更新答案
# 当左边指针长度大于右边的时候，右边加一
# 反之亦然。