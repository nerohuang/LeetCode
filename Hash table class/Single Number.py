class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashset = set() 
        for num in nums:
            if (num not in hashset):
                hashset.add(num)
            else:
                hashset.remove(num)
        return hashset.pop()