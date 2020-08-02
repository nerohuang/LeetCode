class Solution:
    def maxWidthRamp(self, A: List[int]) -> int:
        ans = -1;
        idx = 0;
        minNum = 50001;
        for i in range(len(A)):
            if A[i] >= minNum:
                ans = max(ans, i - idx);
            minNum = min(minNum, A[i]);
            
        return ans;

#Keep a decraesing stack.
#For each number,
#binary search the first smaller number in the stack.
#
#When the number is smaller the the last,
#push it into the stack.
#def maxWidthRamp(self, A):
#    s = []
#    res = 0
#    for i, a in enumerate(A):
#        if not s or A[s[-1]] > a:
#            s.append(i)
#    for j in range(len(A))[::-1]:
#        while s and A[s[-1]] <= A[j]:
#            res = max(res, j - s.pop())
#    return res

#题目大意
#找出最大的j-i，使得i<j并且A[i] <= A[j]。
#
#解题方法
#单调栈
#周赛的时候拿到这个题，第一想法肯定是对于每个数字都去找在它的左边，最远的那个小于等于它的数字。
#然后就很容易分析出，我们想要保存的是每个数字第一次出现的位置，而且依次只用保留最小的即可（数
#字最小才能保证距离最远）。从而就抽象出了单调栈这个数据结构。
#
#这里用到的是单调递减栈，如果遇到一个数字，比栈顶元素更小，那么就入栈；否则就在栈里边向后找到第
#一个刚好小于等于它的元素，此时的距离就是最远距离。