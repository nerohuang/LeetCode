class Solution:
    def numTimesAllBlue(self, light: List[int]) -> int:
        bulb = [0 for _ in range(len(light))];
        ans = 0;
        leftPos = 0;
        for turn in light:
            leftPos = max(leftPos, turn - 1)
            bulb[turn - 1] = 1;
            if 0 not in bulb[:leftPos]:
                ans += 1;
        return ans

#=============上面超时================
#改进，其实思路是一样的，但只要计算左边有几个灯泡亮着
#只要个数和开过的最右边的灯的位置一样那么就代表全开着
#然后ans+1就可以了。


#class Solution:
#    def numTimesAllBlue(self, light: List[int]) -> int:
#        bulb = 0;
#        ans = 0;
#        leftPos = 0;
#        for turn in light:
#            leftPos = max(leftPos, turn)
#            bulb += 1;
#            if bulb == leftPos:
#                ans += 1;
#        return ans
#