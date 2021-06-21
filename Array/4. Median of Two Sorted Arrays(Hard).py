class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            if not nums2:
                return 0
            else:
                if len(nums2) % 2 == 1:
                    return nums2[(len(nums2) // 2)]
                else:
                    return (nums2[(len(nums2) // 2) - 1] + nums2[(len(nums2) // 2)]) / 2
        
        if not nums2:
            if not nums1:
                return 0
            else:
                if len(nums1) % 2 == 1:
                    return nums1[(len(nums1) // 2)]
                else:
                    return (nums1[(len(nums1) // 2) - 1] + nums1[(len(nums1) // 2)]) / 2
            
        total = len(nums1) + len(nums2)    
        newNum = []
        median = total // 2
        while len(newNum) < median + 1:
            if nums1 and nums2:
                if nums1[0] > nums2[0]:
                    newNum.append(nums2.pop(0));
                elif nums1[0] < nums2[0]:
                    newNum.append(nums1.pop(0));
                else:
                    newNum.append(nums1.pop(0));
            elif not nums1:
                newNum.append(nums2.pop(0));
            else:
                newNum.append(nums1.pop(0));
        
        print(newNum)
        
        if total % 2 == 1:
            return newNum[-1]
        else:
            print(newNum)
            return (newNum[-1] + newNum[-2]) /2 

# 思路
# 我合并了一下然后找中位数，但他妈这复杂度是 (m + n) / 2，不屌行。。
# https://www.cnblogs.com/grandyang/p/4465932.html
