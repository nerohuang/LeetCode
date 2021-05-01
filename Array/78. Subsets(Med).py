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

# 这道题是让我们找到所有的subset
# subset是不重复，不连续但是有顺序，所以我们就从1开始遍历
# 其实思路很简单，我们建立一个ans数组来存在第n位之前的所有的subset
# 包括空的，之后在第n位时，我们只要把在这个subset里面的所有的
# array加上n放进一个新的数组，然后再和原来的answer合并，再加上单独
# 一个n，这样我们就有
# [......] + [...n,...n,...n] + [n]
# 这就是我们的新subset。