class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=list(set(nums))
        a=sorted(a)
        
        for i in range(len(a)):
            nums[i]=a[i]
        return len(a)