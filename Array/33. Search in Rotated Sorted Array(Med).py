class Solution:
    def search(self, nums: List[int], target: int) -> int:

        
        if target not in nums:
            return -1;
        
        maxNum = max(nums);
        maxNumIndex = nums.index(maxNum);
        if target == maxNum:
            return maxNumIndex;
        if target > maxNum:
            return -1;
        if target >= nums[0]:
            return bisect.bisect_left(nums,target, lo=0, hi=maxNumIndex);
        if target < nums[0]:
            return bisect.bisect_left(nums,target, lo=maxNumIndex + 1, hi=len(nums));

#class Solution:
#    def search(self, nums: List[int], target: int) -> int:
#        left = 0
#        right = len(nums)-1
#        
#        while(left<=right):
#            
#            mid = (left+right)//2
#            
#            if nums[mid] == target:
#                return mid
#            
#            elif nums[left] <= nums[mid]:
#                if nums[left] <= target and target < nums[mid]:
#                    right = mid - 1 
#                else:
#                    left = mid + 1
#                
#            elif nums[left] > nums[mid]:
#                if nums[right] >= target and nums[mid] < target:
#                    left = mid + 1
#                else:
#                    right = mid - 1
#        
#        return -1

# 其实就是用二分法来找数字，但问题是他多了一个条件，他动过顺序
# 所以要加上判定条件，就是要看出他怎么动的
# 重点是要判断出这个数落在哪一边，所以我们先要找做出判断
# 中位数是否大于最左边，如果是，再判断target是否在nums[left]和nums[mid]之间
# 如果是，那么就就按正常二分法那么做，right = mid - 1；
# 如果不是，那么说明target在 右半段，所以left = mid + 1；
# 如果nums[left] > nums[mid]，那么意思就是转动的个数没有超过一半，这时候就判断
# target是不是在右半边，也就是夹在mid 和 right中间
# 如果是，那么left = mid + 1；
# 如果不是， 那么right = mid - 1；