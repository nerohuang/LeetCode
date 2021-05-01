class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        size = len(nums);
        count = 1;
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
        return len(nums)
                    

# 思路：
# 因为这个只允许时间用o(1)，空间不变，所以我们就要一次处理完
# 那思路很简单，只要重复数多余2那么减少到2就可以了
# 一前一后比较，只要相同然后重复计数大于2的时候，那么就直接remove一个
# 同时count重回2，数组大小因为remove掉一个所以减去1
# 而同时i也要减去一，因为去掉了一个
# 如果重复计数count不大于2，那么i += 1
# 如果不重复，那么复位，count =1， i+=1