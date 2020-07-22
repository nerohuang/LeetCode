class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        if k == 1:
            return [i + 1 for i in range(n)];
        ans = [1];
        order2 = 0;
        order1 = 2;
        for i in range(1, k):
            if i % 2 == 0:
                ans.append(order1);
                order1 += 1;
            else:
                ans.append(n - order2);
                order2 += 1;
        curLast = ans[-1];
        futureLast = ans[-2];
        if k % 2 == 0:
            for i in range(curLast - 1, futureLast, -1):
                ans.append(i);
        else:
            for i in range(curLast + 1, futureLast):
                ans.append(i);
        return ans;


#这道题给我们了一个数字n和一个数字k，让找出一种排列方式，使得1到n组成的数组中相邻两个数
#的差的绝对值正好有k种。给了k和n的关系为k<n。那么我们首先来考虑，是否这种条件关系下，
#是否已定存在这种优美排列呢，我们用一个例子来分析，比如说当n=8，我们有数组：
#
#1, 2, 3, 4, 5, 6, 7, 8
#
#当我们这样有序排列的话，相邻两数的差的绝对值为1。我们想差的绝对值最大能为多少，应该是
#把1和8放到一起，为7。那么为了尽可能的产生不同的差的绝对值，我们在8后面需要放一个小数
#字，比如2，这样会产生差的绝对值6，同理，后面再跟一个大数，比如7，产生差的绝对值5，
#以此类推，我们得到下列数组：
#
#1, 8, 2, 7, 3, 6, 4, 5
#
#其差的绝对值为：7，6，5，4，3，2，1
#
#共有7种，所以我们知道k最大为n-1，所以这样的排列一定会存在。我们的策略是，先按照这种最
#小最大数相邻的方法排列，没排一个，k自减1，当k减到1的时候，后面的排列方法只要按照生序
#的方法排列，就不会产生不同的差的绝对值，这种算法的时间复杂度是O(n)，属于比较高效的那
#种。我们使用两个指针，初始时分别指向1和n，然后分别从i和j取数加入结果res，每取一个数
#字k自减1，直到k减到1的时候，开始按升序取后面的数字.

#class Solution:
#    def constructArray(self, n: int, k: int) -> List[int]:
#        i, j = 1, n
#        res = []
#        while i <= j:
#            if k == 1:
#                res += [x for x in range(i, j + 1)]
#                break
#            elif k == 2 and res:
#                res += [x for x in reversed(range(i, j + 1))]
#                break
#            else:
#                k -= 2 if res else 1
#                res += [j, i]
#                j -= 1
#                i += 1
#        return res