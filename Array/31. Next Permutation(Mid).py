class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if sorted(nums, reverse=True) == nums:
            nums.sort();
        else:    
            maxBigger = 0;
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[i - 1]:
                    maxBigger = i;
                    break;
            for num in sorted(nums[maxBigger - 1:]):
                if num > nums[maxBigger - 1]:
                    secondBiggerIndex = nums[maxBigger - 1:].index(num) + maxBigger - 1;
                    break;
            nums[maxBigger - 1], nums[secondBiggerIndex] = nums[secondBiggerIndex], nums[maxBigger - 1];
            print(nums)
            part2 = sorted(nums[maxBigger:])
            part1 = nums[:maxBigger]
            nums.clear();
            nums.extend(part1);
            nums.extend(part2);

#class Solution:
#    def nextPermutation(self, nums: List[int]) -> None:
#        """
#        Do not return anything, modify nums in-place instead.
#        """
#        i = len(nums) - 1
#        while i > 0 and nums[i - 1] >= nums[i]:
#            i -= 1
#        nums[i:] = sorted(nums[i:])
#        
#        if i > 0:
#            for j in range(i, len(nums)):
#                if nums[j] > nums[i - 1]:
#                    nums[i - 1], nums[j] = nums[j], nums[i - 1]
#                    break

#implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#字典排序，意思就是：像字典一样，先排首字母，然后第二个字母，第三个字母。。。
#2 1 8 7 6 5
#2 5 1 6 7 8
#2 5 1 6 8 7