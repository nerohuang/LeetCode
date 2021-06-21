class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def partition(arr, left, right):
            pivot = left
            j = left + 1
            for i in range(left + 1, right + 1):
                if arr[i] > arr[pivot]:
                    arr[j], arr[i] = arr[i], arr[j]
                    j += 1;
            arr[pivot], arr[j - 1] = arr[j - 1], arr[pivot]
            return j - 1
        
        def quickSort(arr, left = 0, right = len(nums) - 1):
            if left < right:
                pivot = partition(arr, left, right);
                if pivot == k - 1:
                    return arr[pivot]
                elif pivot > k - 1:
                    quickSort(arr, left, pivot - 1);
                else:
                    quickSort(arr, pivot + 1, right)
        
        quickSort(nums)
        return nums[k - 1]

# 思路：
# 这他妈比直接用sort或者heap慢一百倍
# 但可能考点其实就是这个，用快排，然后根据快排每次返回中间值的性质
# 如果放回的index刚好是k位置就返回那个数字，如果index比k-1大
# 那么只排序左边，如果比k-1小，那么排序右半部分
# 当然如果屁都没输出，那么排完再输出

