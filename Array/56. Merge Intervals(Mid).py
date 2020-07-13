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

#class Solution:
#    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#        if intervals == []:
#            return []
#        intervals.sort(key=lambda x: x[0])
#        curr_low, curr_high = intervals[0]
#        result = []
#        for low, high in intervals[1:]:
#            if low > curr_high:
#                result.append([curr_low, curr_high])
#                curr_low, curr_high = low, high
#            else:
#                curr_high = max(curr_high, high)
#        result.append([curr_low, curr_high])
#        return result