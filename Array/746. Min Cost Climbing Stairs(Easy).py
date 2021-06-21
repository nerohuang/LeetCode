class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        
        return cost[-1]

# 经典的爬楼梯问题，也是最简单的dp类，或者是贪心类问题
# 因为一次只能上一级或者两级，所以那么就简单的选最小的类加上去
# 就行了