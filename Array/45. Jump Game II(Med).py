class Solution:
    def jump(self, nums: List[int]) -> int:
        cur = dist = jump = 0;
        
        for i in range(len(nums) - 1):
            dist = max(dist, i + nums[i]);
            
            if i == cur:
                jump += 1;
                cur = dist;
        
        return jump
# 典型的greedy
# dist计算阶梯上能跳得最远的距离
# 然后遍历i，如果i等于当前位置cur，意思就是要继续跳了
# 那么跳跃次数 + 1，然后把下一个目的阶梯替换为dist
