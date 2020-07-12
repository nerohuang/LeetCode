class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sorting is really helpful, se we can avoid over counting easily

    
        def combine_sum(nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider 
        # it as a solution, and stop there
            if not target:
                result.append(path)
                return
        
            for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want 
            # to count the first element in this recursive step even if it is the same 
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
                #if i > start and nums[i] == nums[i - 1]:
                #    continue
            # If the current element is bigger than the assigned target, there is 
            # no need to keep searching, since all the numbers are positive
                if nums[i] > target:
                    break
            # We change the start to `i + 1` because one element only could
            # be used once
                combine_sum(nums, i, path + [nums[i]], result, target - nums[i])
        
        
        candidates.sort()                      
        result = []
        combine_sum(candidates, 0, [], result, target)
        return(result);

#class Solution:
#    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#        res = []
#        if len(candidates) ==0:
#            return []
#        candidates.sort()
#        self.dfs(candidates,[],target,0,res)
#        return res
#        
#        
#    def dfs(self, candidates, subset,target,last, res):
#        if target ==0:
#            res.append(subset[:])
#            return 
#        if target <0:
#            return 
#        if target<candidates[0]:
#            return 
#        for num in candidates:
#            if num > target:
#                return 
#            if num<last:
#                continue
#            subset.append(num)    
#            self.dfs(candidates, subset,target - num,num,res)
#            subset.pop()