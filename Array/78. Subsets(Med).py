class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [];
        newResult = [];
        for num in nums:
            result.append([num]);
            if len(result) >= 2:
                for i in range(len(result) - 1):
                    newResult.append(result[i] + result[-1]);
                result += newResult;
                newResult = [];
        result.append([]);
        return result;


#class Solution:
#    def subsets(self, nums: List[int]) -> List[List[int]]:
#        n = len(nums)
#        output = [[]]
#        
#        for num in nums:
#            output += [curr + [num] for curr in output]
#        
#        return output

#https://leetcode.com/problems/subsets/solution/