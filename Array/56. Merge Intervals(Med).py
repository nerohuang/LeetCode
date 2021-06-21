class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        ans = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(intervals[i][1], ans[-1][1]);
            else:
                ans.append(intervals[i])
                
        return ans

# 思路：
# 遍历即可：
# 如果merged为空或者merged最后一组的后一位大于当前interval的前一位
# merged[-1][1] < interval[0]:
# 那么直接append interval
# 如果不是，那么就对比merged最后一组的后一位和当前interval的后一位
# merged[-1][1] = max(merged[-1][1], interval[1])