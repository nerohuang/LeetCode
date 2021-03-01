class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ans = [1];
        two, three, five =0, 0, 0;
        
        for i in range(n):
            ans.append(min(ans[two] * 2, ans[three] * 3, ans[five] * 5));
            if ans[-1] == ans[two] * 2:
                two += 1
            if ans[-1] == ans[three] * 3:
                three += 1
            if ans[-1] == ans[five] * 5:
                five += 1
        
        return ans[n - 1]

#        analyzation

#initialize
#   ugly[] =  | 1 |
#   i2 =  i3 = i5 = 0;
#
#First iteration
#   ugly[1] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
#            = Min(2, 3, 5)
#            = 2
#   ugly[] =  | 1 | 2 |
#   i2 = 1,  i3 = i5 = 0  (i2 got incremented ) 
#
#Second iteration
#    ugly[2] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
#             = Min(4, 3, 5)
#             = 3
#    ugly[] =  | 1 | 2 | 3 |
#    i2 = 1,  i3 =  1, i5 = 0  (i3 got incremented ) 
#
#Third iteration
#    ugly[3] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
#             = Min(4, 6, 5)
#             = 4
#    ugly[] =  | 1 | 2 | 3 |  4 |
#    i2 = 2,  i3 =  1, i5 = 0  (i2 got incremented )
#
#Fourth iteration
#    ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
#              = Min(6, 6, 5)
#              = 5
#    ugly[] =  | 1 | 2 | 3 |  4 | 5 |
#    i2 = 2,  i3 =  1, i5 = 1  (i5 got incremented )
#
#Fifth iteration
#    ugly[4] = Min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5)
#              = Min(6, 6, 10)
#              = 6
#    ugly[] =  | 1 | 2 | 3 |  4 | 5 | 6 |
#    i2 = 3,  i3 =  2, i5 = 1  (i2 and i3 got incremented )
#我觉得更像是数学题吧。。。