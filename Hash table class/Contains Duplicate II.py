class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {};
        for i in range(len(nums)):
            if nums[i] in store and i - store[nums[i]] <= k:
                return True;
            else:
                store[nums[i]] = i;
        return False;