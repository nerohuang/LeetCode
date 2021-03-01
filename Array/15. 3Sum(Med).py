class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = [];
        nums.sort();
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break;
            if i > 0 and nums[i] == nums[i - 1]:
                continue;
                
            l = i + 1
            r = len(nums) - 1;
            while l < r:
                cur = nums[i] + nums[l] + nums[r];
                
                if cur > 0:
                    r -= 1;
                elif cur < 0:
                    l += 1;
                else:
                    ans.append([nums[i], nums[l], nums[r]]);
                    
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1;
                    
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1;
                    
                    l += 1;
                    r -= 1;
        
        return ans

#思路 
# 拆分， 把他变成一个数字，然后剩下的就是two sum了
# 先排序，这样如果nums[i]>0的时候就说明接下来不会再有三个数之和
# 等于0的存在，break
# 因为不能数字重复使用，所以一前一后如果一样那么就直接跳过，因为
# 那个数的可能性已经被找过了。
# 在two sum的two pointer寻找环节是一个意思。
# 为了避免一样的，只要一左一右有重复的那么就再加减一位。