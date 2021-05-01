class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = [[]];
        nums.sort();
        for num in nums:
            newArray = [];
            for array in ans:
                if array + [num] not in ans:
                    newArray.append(array + [num]);
            ans += newArray;
        return ans

# 思路：
# 和之前做subset是一个思路，不过这次不能有重复的，但是因为有重复
# 数字，所以在加入新数组之前，先检查之前有没有，没有的话就加进去
