class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1;
        size = len(nums);
        i = 1;
        while i < size:
            if nums[i] == nums[i - 1]:
                count += 1;
                if count > 2:
                    nums.remove(nums[i]);
                    size -= 1;
                    count = 2;
                    i -= 1;
                i += 1;
            else:
                count = 1;
                i += 1;

#class Solution:
#    def removeDuplicates(self, nums: List[int]) -> int:
#        j, count = 1, 1
#        for i in range(1, len(nums)):
#            # if duplicate, increase the count
#            if nums[i] == nums[i-1]:
#                count += 1
#            # new element encountered, reset count
#            else:
#                count = 1
#            # for a count <= 2, copy over this element to index "j"
#            if count <= 2:
#                nums[j] = nums[i]
#                j += 1
#        return j