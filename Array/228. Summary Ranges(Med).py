class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        count = 0;
        result = [];
        begin = 0;
        if len(nums) == 1:
            result.append(str(nums[0]));
            return result;
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                count += 1;
                if i == len(nums) - 1:
                    result.append(str(nums[begin]) + "->" + str(nums[i]));
            else:
                if count > 0:
                    result.append(str(nums[begin]) + "->" + str(nums[i - 1]));
                    begin = i;
                    count = 0;
                else:
                    result.append(str(nums[i - 1]));
                    begin = i;
                    count = 0;
                if i == len(nums) - 1:
                    result.append(str(nums[i]));
        return result;

#class Solution:
#    def summaryRanges(self, nums: List[int]) -> List[str]:
#        if not nums:
#            return []
#    
#        range_begin = nums[0]
#        summary = []
#        
#        for i in range(1, len(nums)):
#            if nums[i] - nums[i - 1] > 1:
#                #new range
#                if range_begin == nums[i - 1]:
#                    summary.append(str(range_begin))
#                else:
#                    summary.append(str(range_begin) + "->" + str(nums[i - 1]))
#                
#                range_begin = nums[i]
#            previous = nums[i]
#        if range_begin == nums[-1]:
#            summary.append(str(range_begin))
#        else:
#            summary.append(str(range_begin) + "->" + str(nums[-1]))
#        
#        return summary