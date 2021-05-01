class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        version1 = version1.split('.')
        version2 = version2.split('.')
        v1 = 0
        for i in range(len(version1)):
            s = int(version1[i])
            v1 += (s * 10**-i)
        v2 = 0
        for i in range(len(version2)):
            s  = int(version2[i])
            v2 += (s * 10**-i)
        if v1 > v2:
            return 1
        elif v2 > v1:
            return -1
        else:
            return 0

# 思路：
# 又是实现很有问题
# 只要比较新旧版本， 所以其实只要把版本号转化为
# x.xxxxxx 再比较就可以了。
# 先用split分开所有数字
# 然后重新组成数字。
# 因为小数点之后可以用10^-i来表示。
# 因为不用管leading zero，意思就是 01 和 001
# 是一个东西， 1.01.1 和 1.001.1是一个东西
# 所以这么组成数字肯定是对的。
        