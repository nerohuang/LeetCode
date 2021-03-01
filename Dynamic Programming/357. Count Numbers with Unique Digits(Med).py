class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if not n:
            return 1
        ans = 10;
        for i in range(2, n + 1):
            cur = 9;
            for j in range(i - 1):
                cur *= (9 - j)
            ans += cur;
        return ans;

#他妈的数学题
#第一位是[1-9] 有 9个数字
#第二位是[0-9] 但因为不能重复，所以变成10-1=9个
#第三位是[0-9] 但因为不能重复，所以变成10-2=9个
#如此类推
#在有n位的时候就是
#n =     2   3   4 
#    9 * 9 * 8 * 7 *.. * (9 - n + 2) = (11 - n)
#n = 1的时候是10， n = 2的时候是 10 + 9 * 9
#最后结果就是 10 + (n = 2) + (n = 3) + .....