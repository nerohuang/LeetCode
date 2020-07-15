class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = [];
        resultCount ={1:[], 2:[]};
        newResult = [];
        curResult = [];
        duplicate = False;
        for num in nums:
            result.append([num]);
            if [num] not in resultCount[1]:
                resultCount[1] += [[num]];
            else:
                resultCount[2] += [[num]];
            if len(result) >= 2:
                for i in range(len(result) - 1):
                    newResult.append(result[i] + result[-1]);
                    if sorted(result[i] + result[-1]) not in resultCount[1]:
                        resultCount[1] += [sorted(result[i] + result[-1])];
                    else:
                        resultCount[2] += [sorted(result[i] + result[-1])];
                result += newResult;
                newResult = [];
        result = [[]];
        for ele in resultCount[1]:
            result += [ele];
        return result;

#class Solution:
#def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#    nums.sort()
#    res = []
#    visited = [False] * len(nums)
#    self.dfs(nums, visited, 0, [], res)
#    return res
#
#def dfs(self, nums, visited, start, subset, res):
#    res.append(subset[:])
#    
#    for i in range(start, len(nums)):
#        if i > 0 and nums[i] == nums[i-1] and not visited[i-1]:
#            continue
#        subset.append(nums[i])
#        visited[i] = True
#        self.dfs(nums, visited, i+1, subset, res)
#        subset.pop()
#        visited[i] = False