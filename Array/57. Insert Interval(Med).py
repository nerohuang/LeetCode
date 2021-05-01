class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            intervals.append(newInterval)
            return intervals;
        
        intervals.append(newInterval);
        intervals.sort();
        
        ans = [];
        
        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval);
            else:
                ans[-1][1] = max(ans[-1][1], interval[1]);
                
        return ans;

# 思路：
# 把新的塞进去，然后用56的思路做。。。
