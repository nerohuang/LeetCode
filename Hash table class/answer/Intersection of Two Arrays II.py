class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 1st try. 3rd requirement should be cared. ARS.
        ## Dual pointer. Very pretty
        nums1, nums2 = sorted(nums1), sorted(nums2)
        result = []
        p1 = p2 = 0
        while True:
            try:
                if nums1[p1] == nums2[p2]:
                    result.append(nums1[p1])
                    p1 += 1
                    p2 += 1
                elif nums1[p1] < nums2[p2]:
                    p1 += 1
                else:
                    p2 += 1
            except IndexError:
                break
        return result