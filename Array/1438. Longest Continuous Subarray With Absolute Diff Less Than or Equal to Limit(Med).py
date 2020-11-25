class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        # left and right index for tracing out current subarray
        l = 0
        r = 1
        # number out of this may only create problem
        cur_mx = nums[0]
        cur_mn = nums[0]
        # atleast max_l = 1, bcoz [8] = 8-8 = 0 <= limit
        max_l = 1
        # since, it is like sliding window ques,
        # use while loop with left, right index
		# with for loop it will be complicated
        while l <= r and r < len(nums):
            cur_mx = max(cur_mx, nums[r])
            cur_mn = min(cur_mn, nums[r])

            if cur_mx - cur_mn <= limit:
                max_l = max(max_l, r - l + 1)
            else:
                if nums[l] == cur_mx:
                    # need to update cur_mx
                    cur_mx = max(nums[l + 1:r + 1])  # inclusive r
                # using if & not elif bcoz- nums[l] == cur_mn == cur_mx
                if nums[l] == cur_mn:
                    # need to update cur_mn
                    cur_mn = min(nums[l + 1:r + 1])
                l += 1
            r += 1
        return max_l

#思路：用sliding windows。先设定cur_mx和cur_mn为nums第一个数。
#然后开始结合two pointer进行while loop：
#第一步先确认右边的新数字会不会是当前最大或者最小。
#无论有没有更新最大最小值，都会将当前最大cur_mx减去cur_mn来判断
#有没有超出limit，如果没有，那说明当前window里面所有数相减的绝对值
#都不会超过limit，然后update答案最大值。
#如果超出了，那么判断两种情况：
#第一种：如果left所指的数是当前最大的数cur_mx，那么就要重新在新的区
#间更新cur_mx。
#第二种：如果left所指的数是当前最小的数cur_mn，那么就要重新在新的区
#间更新cur_mn。
#判断完之后要记得将left+1往右移一位。

#有用deque做的第二种比较快的方法：

#class Solution:
#    def longestSubarray(self, nums: List[int], limit: int) -> int:
#        #O(n^2)time before having to calc. min/max(nums[l:r]) every iteration
#        #min and maxQs bring time/space to O(n), O(n)
#        #minQ keeps Q of minimum elt. up to nums[r]
#        # eg (2,3,4,5 r=3) => (2,3,3)
#        minQ = collections.deque()
#        #maxQ keeps Q of max elt. up to nums[r]
#        # eg (5,4,3,2 r=3) => (5,4,3,3)
#        maxQ = collections.deque()
#        n = len(nums)
#        r = l = res = 0
#        while r < n:
#            #if window size 1 or valid, extend r
#            if l==r or abs(nums[r]-minQ[0])<=limit and abs(maxQ[0]-nums[r])<=limit:
#                #cleans up minQ and maxQ so it correctly stores min/max elts
#                while minQ and nums[r]<minQ[-1]:
#                    minQ.pop()
#                while maxQ and nums[r]>maxQ[-1]:
#                    maxQ.pop()
#                #append @ correct location
#                minQ.append(nums[r])
#                maxQ.append(nums[r])
#                
#                r+=1
#                res = max(res, r-l)
#            #else, extend l
#            else:
#                # if lhs to remove is smallest elt.
#                if nums[l] == minQ[0]:
#                    minQ.popleft()
#                # if lhs to remove is biggest elt.
#                if nums[l] == maxQ[0]:
#                    maxQ.popleft()
#                l+=1
#        return res