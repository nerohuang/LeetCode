class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x: x[1], reverse = True)
        ans = 0;
        
        for boxes, units in boxTypes:
            if boxes <= truckSize:
                ans += boxes * units
                truckSize -= boxes
            else:
                ans += truckSize * units
                break
        
        return ans

# 思路
# 贪心
# 思路就是尽可能得放入preUnit更大得箱子
# 很简单的一个贪心