class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures);
        higherTemperaturesLocation = [];
        
        for i in range(len(temperatures)):
            while higherTemperaturesLocation and temperatures[higherTemperaturesLocation[-1]] < temperatures[i]:
                temperatureLocation = higherTemperaturesLocation.pop();
                ans[temperatureLocation] = i - temperatureLocation
            higherTemperaturesLocation.append(i)
        
        return ans

# 思路：
# 整体思路是对的，但是重点是用到栈，或者，是从后到前而不是
# 从前到后
# 为什么是从后到前，举个例子：
#  [73, 74, 75, 71, 69, 72, 76, 73]
# 我们会发现第一组出现需要等待的温度是从75开始到69，所以我们会有
# [75, 71, 69]
# 到了72，我们开始判断之前是否有小于72的数字
# 如果我们从前开始遍历，那么会多一个75的时间，才能相继找到71，69
# 如果我们从69开始，那么我们找到75的时候就可以break了， 因为75
# 往前的数字只能比75大，不可能比75小，那么再寻找毫无意义
# 之前我觉得可能会出现一种[75, 70, 71, 69]的情况，但认真想想是
# 不可能的，因为71就已经比70大了，不会出现在接下来72需要寻找的
# 栈中。
