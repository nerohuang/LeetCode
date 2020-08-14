class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ans = 0;
        for i in range(len(customers)):
            if grumpy[i] == 0:
                ans += customers[i];
                customers[i] = 0;
        resList = [];
        res = 0;
        for i in range(X):
            res += customers[i];
        resList.append(res);
        for i in range(X, len(customers)):
            res += customers[i] - customers[i - X];
            resList.append(res);
        
        return ans + max(resList);

#思路：
#首先把只要grumpy数值中为0的，对应相同位置的customers的值相加并替换为0：
#[1,0,1,2,1,1,7,5]
#[0,1,0,1,0,1,0,1]
#替换后：
#[0,0,0,2,0,1,0,5]
#
#然后再这个替换后的数组里面找到窗口范围X里面和最大的值，然后和之前得到的和相加