#class Solution:
#    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#        def findSum(l ,r, target, n, result, results):
#            if r - l + 1 < n or target < candidates[l] * n or target > candidates[r] * n:
#                return;
#            if n == 2:
#                while l < r:
#                    s = candidates[l] + candidates[r];
#                    if s == target:
#                        results.append(result + [candidates[l], candidates[r]]);
#                        l += 1;
#                        while l < r and candidates[l] == candidates[l - 1]:
#                            l += 1;
#                    elif s < target:
#                        l += 1;
#                    else:
#                        r -= 1;
#            else:
#                for i in range(l, r + 1):
#                    if i == l or (i > l and candidates[i - 1] != candidates[i]):
#                        findSum(i + 1, r, target - candidates[i], n - 1, result + [candidates[i]], results);
#
#        candidates.sort();
#        results = [];
#        if target in candidates:
#            results.append([target]);
#        if len(candidates) == 2:
#            if candidates[0] + candidates[1] == target:
#                results.append([candidates[0], candidates[1]]);
#        for i in range(2, len(candidates)):
#            findSum(0, len(candidates)-1, target, i, [], results);
#        return(results);

candidates = [2,3,6,7]
target = 7
#lut = [set() for i in range(target+1)]
#lut[0] = {()}
#candidates.sort()
#for cand in candidates:
#    for i in range(target, cand-1, -1):
#        for ans in lut[i-cand]:
#            lut[i].add(ans+(cand,))
#print(lut[target])


#class Solution:
#    def combinationSum2(self, candidates, target):
#        # Sorting is really helpful, se we can avoid over counting easily
#
#    
#        def combine_sum_2(nums, start, path, result, target):
#        # Base case: if the sum of the path satisfies the target, we will consider 
#        # it as a solution, and stop there
#            if not target:
#                result.append(path)
#                return
#
#            for i in range(start, len(nums)):
#            # Very important here! We don't use `i > 0` because we always want 
#            # to count the first element in this recursive step even if it is the same 
#            # as one before. To avoid overcounting, we just ignore the duplicates
#            # after the first element.
#                if i > start and nums[i] == nums[i - 1]:
#                    continue
#            # If the current element is bigger than the assigned target, there is 
#            # no need to keep searching, since all the numbers are positive
#                if nums[i] > target:
#                    break
#            # We change the start to `i + 1` because one element only could
#            # be used once
#                combine_sum_2(nums, i + 1, path + [nums[i]], result, target - nums[i])
#
#
#        candidates.sort()                      
#        result = []
#        combine_sum_2(candidates, 0, [], result, target)
#        print(result);