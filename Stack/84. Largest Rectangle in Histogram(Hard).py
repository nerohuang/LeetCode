heights = [1,2,3,4,5,6]
           
heights.append(0)
stack = [-1]
ans = 0
for i in range(len(heights)):
    while heights[i] < heights[stack[-1]]:
        height = heights[stack.pop()]
        width = i - stack[-1] - 1
        ans = max(ans, height * width)
    stack.append(i)
heights.pop()

# 思路：
# 一个东西，单调递增栈，真的很妙
# 思路就是维持一个单调递增的栈，如果碰到新的高度比栈最后一位
# 也就是最大的一位小的话，那么就开始pop，直到能重新组成单调
# 递增数列位置，而这时候pop出来的高度则用于计算最大面积并更新
# 再开始之前最后一位要加上0，防止本身给出的数据就算是个单调
# 递增。
