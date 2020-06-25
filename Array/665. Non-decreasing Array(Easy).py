class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        index = 0;
        count = 0;
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1;
                index  = i;
                if count > 1:
                    return False;
        #预防[3,4,2,3]这种情况
        return (index == 0 or index == len(nums)-2 or nums[index-1] <= nums[index+1] or nums[index] <= nums[index+2]);

##class Solution:
##    def checkPossibility(self, nums: List[int]) -> bool:
##        length = len(nums)
##        count = 0
##        for i in range(1,length):
##            #print(nums[i] - nums[i-1])
##            if nums[i] - nums[i-1] < 0:
##                count += 1
##                # 特殊情况.
##                if i-2 >=0 and i+1 < length:
##                    #[3,4,2,3] 4 < 2 所以要么把2放大，并且保证 2后面的元素要>= 4，要么就是4缩小 4前面的都要<= 2
##                    if nums[i+1] <nums[i-1] and nums[i] < nums[i-2]: # 注意是and 不是 or
##                        return False
##            if count > 1:
##                return False
##            
##        return True