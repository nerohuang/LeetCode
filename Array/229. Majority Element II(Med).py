class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums);
        countNum = {};
        result = [];
        for num in nums:
            if num not in countNum:
                countNum[num] = 1;
            else:
                countNum[num] += 1;
            if countNum[num] == (n//3) + 1:
                result.append(num);
        return result;

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k=list(dict.fromkeys(nums))
        a=[]
        for i in k:
            if nums.count(i) > len(nums)//3:
                a.append(i)
        return a        