class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        ans = 0;
        for i in range(len(arr) - 1):
            a = arr[i]
            for j in range(i + 1, len(arr)):
                if j - 1 != i:
                    a ^= arr[j - 1]
                b = arr[j];
                for k in range(j, len(arr)):
                    if j != k:
                        b ^= arr[k];
                    if a == b:
                        ans += 1;
        return ans




#class Solution:
#    def countTriplets(self, arr: List[int]) -> int:
#        n = len(arr)
#        output = 0
#        for i in range(n):
#            xor = arr[i]
#            for j in range(i + 1, n):
#                xor = xor ^ arr[j]
#                if xor == 0:
#                    
#                    output += j - i
#        return output

#更快的思路:
#首先要知道：
# a xor b == 0 if a == b
# 所以其实这题目就是 arr[i] ^ ... ^arr[k] == 0
# 所以只要当当前累计的xor等于0， 那么在这个区间内的数字个数
# 就是那个区间（i, j, k）组合数量的个数。