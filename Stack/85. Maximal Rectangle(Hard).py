matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]

def calArea(heights):
    heights = [0] + heights + [0]
    stack = []
    maxArea = 0
    for i, h in enumerate(heights):
        while(stack and heights[stack[-1]] > h):
            j = stack.pop()
            maxArea = max(maxArea, (i-stack[-1]-1)*heights[j])
        stack.append(i)
    return maxArea

heights = [0] * len(matrix[0])
ret = 0

for row in matrix:
    for i, v in enumerate(row):
        heights[i] = heights[i]+1 if v == '1' else 0
    maA = calArea(heights)
    ret = max(ret, maA)

# 思路：
# 其实是84的延申
# 每一列累积的高度，表明
