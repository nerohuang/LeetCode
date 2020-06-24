class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {};
        for num in nums:
            if num in count.keys():
                count[num] += 1;
            else:
                count[num] = 0;
        return max(count, key=count.get)

##class Solution:
##  def majorityElement(self, nums: List[int]) -> int:
##      if len(nums) == 1:
##          return nums[0]
##      
##      nums.sort()
##      return nums[len(nums)//2]