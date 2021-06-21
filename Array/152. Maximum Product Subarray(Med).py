#class Solution:
#    def maxProduct(self, A):
#        B = A[::-1]
#        for i in range(1, len(A)):
#            A[i] *= A[i - 1] or 1
#            B[i] *= B[i - 1] or 1
#        return max(A + B)
#
# 这事一种思路，不太常见
# 思路是进行两种累乘，一种是正向，一种是反向
# 如果碰到0，那么就乘以1继续
# 这种正反向是为了防止有奇数个负数
# 因为负数可能会把最大值和最小值翻转，那么当有奇数个负数时，
# 如果只是正向遍历的话，可能会出错，
# 比如 [-1, -2, -3]，累加积会得到 -1，2，-6，看起来最大值只能为2，其实不对，
# 而如果我们再反向来一遍，累加积为 -3，6，-6，就可以得到6了。所以当负数个数为奇数时，
# 首次出现和末尾出现的负数就很重要，有可能会是最大积的组成数字，所以遍历两次就不会漏掉组成最大值的机会，

#def maxProduct(self, nums: List[int]) -> int:
#    curr_max = global_max = curr_min = nums[0]
#    
#    for i in range(1, len(nums)):
#        curr_max, curr_min = max(nums[i], nums[i] * curr_max, nums[i] * curr_min), min(nums[i], nums[i] * curr_max, nums[i] * curr_min)
#        global_max = max(global_max, curr_max)
#
#
#    return global_max

# 第二种方法：
# 最大子数列问题，可以参考一下，然后就是要注意怎么处理0这个数了
# https://www.cnblogs.com/grandyang/p/4028713.html