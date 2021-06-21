class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval);
        intervals.sort();
        ans = [intervals[0]];
        
        for i in range(len(intervals)):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1]);
            else:
                ans.append(intervals[i])
                
        return ans

# 思路：
# 把新的塞进去，然后用56的思路做。。。
