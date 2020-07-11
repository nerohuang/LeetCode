class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = -9999999999999999999999999999999;
        nums.sort();
        length = len(nums)
        for i in range(length - 2):
            if nums[i] > target and i <= length - 2:
                curTotal = nums[i] + nums[i + 1] + nums[i + 2];
                if abs(curTotal - target) < abs(ans - target):
                    ans = curTotal;
                
            l, r = i + 1, length - 1;
            while l < r:
                curTotal = nums[i] + nums[l] + nums[r];
                if curTotal - target < 0:
                    l += 1;
                    if abs(curTotal - target) < abs(ans - target):
                        ans = curTotal;
                elif curTotal - target  > 0:
                    r -= 1;
                    if abs(curTotal - target) < abs(ans - target):
                        ans = curTotal;
                else:
                    return curTotal;
        return ans;

#class Solution:
#    def threeSumClosest(self, nums, target):
#        nums.sort()
#        absdis = float("inf")  # record abs
#        diff = 0  # save sum3-target
#        k = len(nums)
#        n = nums
#        t = target
#        rr = k - 2
#        for i in range(k - 2):
#            j = i + 1
#            r = k - 1
#            # 两种边界判断
#            j2 = i + 2
#            small = n[i] + n[j] + n[j2]
#            if small == t:
#                return t
#            elif small > t:  # n[i] 已经很大了，不用再循环了。
#                if small - t < absdis:
#                    return small
#                else:
#                    return t + diff
#            elif small < t:
#                # check the big from this n[i]
#                big = n[i] + n[rr] + n[r]
#                if big == t:
#                    return t
#                elif big < t:
#                    # 尝试更新
#                    temp = t - big
#                    if temp < absdis:
#                        absdis = temp
#                        diff = -temp
#                elif big > t:
#                    # 需要双指针查找，并更新absdis
#                    while j < r:
#                        a = n[i] + n[j] + n[r]
#                        if a == t:
#                            return a
#                        elif a > t:
#                            # # refresh absdis and diff if need
#                            if a - t < absdis:
#                                absdis = a - t
#                                diff = absdis
#                            #r -= 1  add slide when two nums are same
#                            k0 = r - 1
#                            while j < k0 and n[k0] == n[r]:
#                                k0-=1
#                            r=k0
#
#                        elif a < t:
#                            if t - a < absdis:
#                                absdis = t - a
#                                diff = -absdis
#                            
#                            jj=j+1
#                            while jj<r and n[jj]==n[j]:
#                                jj+=1
#                            j=jj
#                            
#        return t + diff