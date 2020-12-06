class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, ans = 0, 0, 0;
        for num in arr:
            if num % 2 == 1:
                odd, even = even + 1, odd;
            else:
                odd, even = odd, even + 1;
            ans += odd;
        return ans % int(1e9 + 7)

#思路:
#我们建立一个odd和even分别储存 以当前数字为结尾的，和是odd和even的substring：
#我们来看看： [1,2,3,4,5]
#以4为结尾的：        
#odd = [3,4]
#    = [2,3,4]
#even = [4]
#     = [1,2,3,4]
#当以5做结尾时，我们知道sum要是奇数那只能奇数+偶数：
#odd = [5]
#    = [4, 5]
#    = [2,3,4,5]
#even = [3,4,5]
#     = [1,2,3,4,5]
#可以看出当遍历到奇数的时候，就把前一个数的even子序列加上自己，所以就是
#odd[5] = even[4] + 1
#而偶数数量则不变：
#even[5] = odd[4];
#再看看6：
#odd = [5,6]
#    = [4,5,6]
#    = [2,3,4,5,6]
#even = [3,4,5,6]
#     = [1,2,3,4,5,6]
#     =[6]
#可以看出当遍历到偶数的时候，就把前一个数的even子序列加上自己，所以就是
#even[6] = even[5] + 1
#而奇数数列总数不变：
#odd[6] = odd[6];