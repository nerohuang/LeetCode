class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {};
        result = [];
        if len(nums2) > len(nums1):
            return self.intersect(nums2, nums1);
        else:
            for i in nums1:
                if i not in m:
                    m[i] = 1;
                else:
                    m[i] += 1;
            for i in nums2:
                if (i in m) and (m[i] > 0):
                    m[i] -= 1;
                    result.append(i);
            return result;