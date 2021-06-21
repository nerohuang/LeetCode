class Solution:
    def numSubarrayBoundedMax(self, A: List[int], L: int, R: int) -> int:
        store = [];
        for i in range(len(A)):
            curStore = [];
            j = i;
            while j < len(A) and A[j] <= R:
                curStore.append(A[j]);
                if max(curStore) >= L:
                    newStore = curStore.copy();
                    store.append(newStore);
                j += 1;
        return(len(store)); 


#class Solution:
#    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
#        ans = 0
#        l = -1
#        r = -1
#        for i, num in enumerate(nums):
#            if num > right:
#                l = i
#            if num >= left:
#                r = i
#            ans += r - l
#        return ans

# 思路
# 第一次做这个题的思路其实就是遍历所有了，所以花的时间
# 很长，这样不行，所以正确做法是用一个slide windows来做
# l,r 分别是windows的左右两端
# 当遍历到的数字比left要大的时候，那么r就往前走一位
# 然后和再计算l - r，这是计算从l 开始到 r有多少个
# 以r 为起点不一样的subarray 然后累加即可
# 如果碰到num大于等于r，那么r就回到和l一样的位置
# 因为right大于left，如果num大于right必然也大于left
# 然后就等于重置了windows
# 当如果遇到小于left的，那么
# 举个例子 [3, 1, 4, 5, 2, 7, 3]
# left是2，right 是6
# 这样的话我们第一个是3
# r前进一格，那么就是单独一个[3]，ans + 1
# 然后再前进一格，是1，但是小于left，但是[3 ,1]
# 最大值是3，所以也满足，但是也只有一个[3, 1]
# 所以延续之前的l 和 r, 再加一次就可以了
# 然后就这么一路到7，重置
# l,r都是到5， 然后继续