class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        nums.sort();
        count = {};
        for num in nums:
            count[num] = count.get(num, 0) + 1;
        for num in nums:
            while count[num] > 0:
                for i in range(k):
                    if count.get(num + i, 0)> 0:
                        count[num + i] -= 1;
                    else:
                        return False
        return True;

#用dict来压缩时间