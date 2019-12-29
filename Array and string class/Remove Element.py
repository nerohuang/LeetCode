class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        i = 0
        for j in range(len(nums)):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
            print(i, nums)