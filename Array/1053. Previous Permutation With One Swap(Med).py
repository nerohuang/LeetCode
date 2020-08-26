class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        p1 = -1;
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                p1 = i;
                break;
        if p1 == -1:
            return A;
        p2 = p1 + 1;
        for i in range(p1 + 1, len(A)):
            if (A[p1] > A[i]) and (A[p2] < A[i]):
                p2 = i;
        A[p1], A[p2] = A[p2], A[p1]
        return A


#拿到这道题，首先分析题意，题目给了我们一个包含正整数的数组，让我们在数组中进行一次数字交换，
#交换后的排列要比原排列字典序小，但是交换后的排序又是所有满足条件的序列中字典序最大的，于是
#我们分析： 对于一个数来说，如果让我们交换数字中的两个数让交换的数比原数小，最直接的就是把最
#高位上的数减小，但是还要满足交换后的数是比原数小的最大的数，那么就不能从最高位开始交换，而是
#从最低位改变，这样对于原数的影响才最小。
#
#比如6534，我们从后往前判断，找一个数（满足该数后存在比其小的数），发现在5上改变对原数影响最小，
#只需要从5后面的数中选一个比5小的数把5换掉即可，但是5后面可能有很多比5小的数字，选取哪一个数字
#来和5交换呢？从贪心来看我们肯定想找一个比5小一点点的数字，这样对原数减小的程度才最小，也就是
#小于5的所数中最大的那个数，这里是4。
#
#于是可以把算法分成三个步骤：
#
#步骤1： 首先从后往前找到第一个满足比其后数字大的数，如果不存在，说明该数无法通过交换来减小，
#法结束，否则转步骤2；
#步骤2: 从步骤1中找到的数往后找比该数小的最大数位置；
#步骤3: 交换步骤1和步骤2找的两个索引上对应的数；