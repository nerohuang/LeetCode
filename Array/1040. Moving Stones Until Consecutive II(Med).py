class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        stones.sort()
        i, n, lower = 0, len(stones), len(stones)
        upper = max(stones[-1] - n + 2 - stones[1], stones[-2] - stones[0] - n + 2)
        for j in range(n):
            while stones[j] - stones[i] >= n: 
                i += 1
            if j - i + 1 == n - 1 and stones[j] - stones[i] == n - 2:
                lower = min(lower, 2)
            else:
                lower = min(lower, n - (j - i + 1))
        return [lower, upper]


#题目要求求出让石头堆连续排列的最大和最小移动步数。我们需要将最大和最小移动步数分成两个问题考虑。
#将总共的石头堆的数目用n表示。另外，我们首先需要做预处理，将给我们的array做个排序。
#
#对最大移动步数，用贪心的思想，要么都移动到最左端，要么都移动到最右端。我们需要考察stones[n-2]
#到stones[0]和stones[n-1]到stones[1]的间距，进行比较。在这两个选择中。选择空的position最多的
#那个。同时，因为一开始需要将一个endpoint做一次移动，所以需要额外加上这次步骤。
#
#    比如有一组：
#    0..0.00..00
#    最多移动的方法就是
#    最右边的那个0往左移一下，然后二人转：
#    step 0:
#    0..0.00..00
#              |
#    step 1:
#    0..0.00.00
#             |
#    step 2:
#    0..0.0000
#    .
#    .
#    .
#    step n - 1:
#    0.00000
#    step n:
#    000000
#    所以步数就是倒数第二个和第一个比较，然后倒数第一个和第二个比较间距（中间有多少个空）
#    选空格多的那个。
#
#对最小移动步数，用sliding window 的方法。window的长度是n。计算每个window中，最多已经被填满
#的空间数量。剩下的未被填满的空间就是最小的移动数目。
#
#需要额外注意的是，这里存在一种corner case违背了上述的结论，需要特殊处理。举例如下：
#如果石头堆是1，2，3，6, 那么n是4，对于第一个window，它有一个空位置，在4， 但是6不能移动到4，
#这不是一个valid move，所以必须将1 移动到5，6移动到4，必须至少2步才能完成要求。
#
#也就是说，当一个window的长度是n，它包含了连续的n-1个非空位，同时这n-1个非空位在原来石头堆的位
#置也是连续的，那我们就需要2步才能完成石头堆的最小移动。