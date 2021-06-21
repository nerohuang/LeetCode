class Solution:
    def trap(self, heights: List[int]) -> int:
        leftMaxHeight = 0;
        rightMaxHeight = 0;
        left = 0;
        right = len(heights) - 1;
        ans = 0;
        
        while left < right:
            if heights[left] < heights[right]:
                if heights[left] >= leftMaxHeight:
                    leftMaxHeight = heights[left]
                else:
                    ans += leftMaxHeight - heights[left]
                left += 1;
            else:
                if heights[right] >= rightMaxHeight:
                    rightMaxHeight = heights[right]
                else:
                    ans += rightMaxHeight - heights[right]
                right -= 1;
                
            
        return ans

# 思路，two pointer
# 一左一右往中间走，这是还会有三种情况，我们化为两种：
# 1，heights[left] < heights[right]:
# 这种情况下，因为水坑是取决于较小的边，那么继续从左到右遍历
# 我们要看看 这个时候heightsp[left] 是否大于了之前存的左边最大值
# leftMaxHeight，如果大于了，那么就更新最大值，并且不需要填坑
# （因为之前的坑在便利的时候已经填完了）
# 如果不是大于leftMaxHeight，那么我们就要相减高度得出我们要填
# 的面积是多少
# 然后左指针前向推进1
# 2， heights[left] >= heights[right]
# 这种情况下，我们要变换思路，因为这时候heights[right]是小于
# heights[left]，遵循之前水坑取决于较小的边，这时候我们就要反
# 过来推算