class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if timeSeries == []:
            return 0;
        begin = timeSeries[0];
        end = timeSeries[0] + duration;
        totalTime = 0;
        for i in range(1, len(timeSeries)):
            if timeSeries[i] <= end:
                end = timeSeries[i] + duration;
            else:
                totalTime += end - begin;
                begin = timeSeries[i];
                end = timeSeries[i] + duration;
        
        if timeSeries[-1] <= end:
            end = timeSeries[-1] + duration;
            totalTime += end - begin;
        return totalTime

#class Solution:
#    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
#        curr = 0
#        prev = timeSeries[0] if timeSeries else -1
#        for t in timeSeries:
#            if t - prev > duration:
#                curr += duration
#            else:
#                curr += t - prev
#            prev = t
#        if prev >= 0:
#            curr += duration
#        return curr

#class Solution(object):
#    def findPoisonedDuration(self, timeSeries, duration):
#        ans = duration * len(timeSeries)
#        for i in range(1,len(timeSeries)):
#            ans -= max(0, duration - (timeSeries[i] - timeSeries[i-1]))
#        return ans