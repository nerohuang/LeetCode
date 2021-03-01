class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx =0, 0;
        for i in range(len(s1)):
            if s1[i] == "x" and s2[i] == "y":
                xy += 1;
            if s1[i] == "y" and s2[i] == "x":
                yx += 1;
        
        if xy % 2 == 0 and yx % 2 == 0:
            return (xy + yx)//2;
        
        if xy % 2 == 1 and yx % 2 == 1:
            return (xy + yx)//2 + 1;
        
        return -1

#思路：
#贪心，这种调换只有两种情况：
#1）当（xx，yy）的时候，只需要调换一次
#2）当（xy，yx）的时候，需要调换两次。
#所以思路就是先把不同的字母先按第一种调换完
#然后剩下就按第二种。
#所以先找出所有不同位置的情况并记录：xy，yx
#先判断，如果xy和yx的个数都为偶数，说明他们只要
#执行第一种方法就能互相调整完毕:
#x y y x
#y x x y => 这种情只需要调整 （2 + 2）//2次。
#如果xy和yx的个数都为奇数，说明他们用第一种方法
#调整完之后还剩下一个，而这个就需要用第二种调整方法：
#x x x y y
#y y y x x => 调整完第一种情况之后会剩下一组（x,y）
#             这时候就要额外加一步完整调整
#当xy和yx的个数相加为奇数的时候，他们并不可能
#调整完之后达成两边一样，所以输出-1.