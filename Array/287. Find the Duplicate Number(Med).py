class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        store = {};
        for num in nums:
            if num not in store:
                store[num] = 1;
            else:
                return num;

#Floyd's Tortoise and Hare (Cycle Detection)
#class Solution:
#    def findDuplicate(self, nums):
#        # Find the intersection point of the two runners.
#        tortoise = hare = nums[0]
#        while True:
#            tortoise = nums[tortoise]
#            hare = nums[nums[hare]]
#            if tortoise == hare:
#                break
#        
#        # Find the "entrance" to the cycle.
#        tortoise = nums[0]
#        while tortoise != hare:
#            tortoise = nums[tortoise]
#            hare = nums[hare]
#        
#        return hare