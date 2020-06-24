class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ##nums.sort();
        nums_set = set(nums);
        nums_list = list(nums_set)
        whole_list = [];
        for i in range(len(nums)):
            whole_list.append(i + 1);
        return (list(set(whole_list) - set(nums_list)))

##class Solution:
##    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
##        n, res = len(nums), []
##        nums = set(nums)
##        for i in range(1, n+1):
##            if i not in nums:
##                res.append(i)
##        return res