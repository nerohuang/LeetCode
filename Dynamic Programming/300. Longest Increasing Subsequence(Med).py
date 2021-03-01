class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))];
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1);
        
        return max(dp)

#dp思路：
#建立一个等长的dp数组，初始值都为1.
#dp[i] 代表含第 i 个元素的最长上升子序列的长度。
#思路就是先从第二位开始遍历刀最后一位，为i
#然后嵌套，从0到i-1位
#然后将nums[i]和nums[j]进行对比
#因为是寻找最长上升序列，所以当nums[i]>nums[j]
#的时候，就开始比较dp[i]和dp[j]+1；
#这种比较就是dp[i]就是在第i位前面能有多少个数小于他
#dp[j] + 1则是因为nums[i]>nums[j]，这样的话最长序列
#就会增加1，然后这两个比较看谁大就替换掉原来的那个。
#https://leetcode.com/problems/longest-increasing-subsequence/solution/

#很具小巧思。新建数组 cell，用于保存最长上升子序列。
#
#对原序列进行遍历，将每位元素二分插入 cell 中。
#
#如果 cell 中元素都比它小，将它插到最后
#否则，用它覆盖掉比它大的元素中最小的那个。
#总之，思想就是让 cell 中存储比较小的元素。这样，cell 
# 未必是真实的最长上升子序列，但长度是对的。

#class Solution:
#    def lengthOfLIS(self, nums: List[int]) -> int:
#        size = len(nums)
#        if size<2:
#            return size
#        
#        cell = [nums[0]]
#        for num in nums[1:]:
#            if num>cell[-1]:
#                cell.append(num)
#                continue
#            
#            l,r = 0,len(cell)-1
#            while l<r:
#                mid = l + (r - l) // 2
#                if cell[mid]<num:
#                    l = mid + 1
#                else:
#                    r = mid
#            cell[l] = num
#        return len(cell)n