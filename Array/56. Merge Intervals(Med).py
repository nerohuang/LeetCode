class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort()

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

# 思路：
# 遍历即可：
# 如果merged为空或者merged最后一组的后一位大于当前interval的前一位
# merged[-1][1] < interval[0]:
# 那么直接append interval
# 如果不是，那么就对比merged最后一组的后一位和当前interval的后一位
# merged[-1][1] = max(merged[-1][1], interval[1])