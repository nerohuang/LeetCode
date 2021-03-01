class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) != len(set(timePoints)):
            return 0;
        
        def calMin(timePoints):
            ans = 1441;
            for i in range(1, len(timePoints)):
                different = (int(timePoints[i][:2]) - int(timePoints[i - 1][:2])) * 60 + (int(timePoints[i][3:]) - int(timePoints[i - 1][3:]))
            
                ans = min(ans, different);
            
            return ans;
        
        timePoints.sort();
        timePoints.append(timePoints[0]);
        timePoints[-1] = str(24 + int(timePoints[-1][:2])) + ':' + timePoints[-1][3:];
            
        ans = calMin(timePoints);
        
        return ans

#思路
#先排序，然后把排序后的第一个加到最后一位
#这样就相当于形成一个闭环，所有都可以计算到
#加入的同时，加上24小时，防止负数：
#["01:39","10:26","21:43"]
#变成
#["01:39","10:26","21:43", "25:39"]