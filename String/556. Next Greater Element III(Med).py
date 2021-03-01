class Solution:
    def nextGreaterElement(self, n: int) -> int:
        numList = list(str(n));
        i = len(numList) - 1;
        while i and numList[i] <= numList[i - 1]:
            i -= 1;
        if not i:
            return -1;
        for i in range(len(numList) - 1, 0, -1):
            if numList[i] > numList[i - 1]:
                location = i;
                break;
        numList = numList[:location] + numList[location:][::-1];
        for i in range(location, len(numList)):
            print(numList)
            print(location)
            if numList[i] > numList[location - 1]:
                numList[i], numList[location - 1] = numList[location - 1], numList[i];
                break;
        ans = int("".join(numList));
        if ans > 2147483647:
            return -1
        else:
            return ans


#思路：
#先找到从后向前数，第一个降序的位置，把此位置后面的翻转。
# 再把这个降序数字和后面第一个比它大的位置交换即可。
# 如果从第n个数字到最后都是递减的并且第n-1个数字小于第n个，
# 说明从第n个数字开始的这段序列是字典序组合的最后一个，在
# 下一个组合中他们要倒序变为字典序第一个，然后从这段序列中
# 找出第一个大于第n-1个数字的数和第n-1个数字交换就可以了。

# 举个栗子，当前组合为12431，可以看出431是递减的，同时4>2，
# 这样我们把431倒序，组合就变为12134，然后从134中找出第一
# 个大于2的数字和2交换，这样就得到了下一个组合13124。对于
# 完全递减的组合例如4321在倒序之后就可以结束了。