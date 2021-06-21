class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        def binarySearch(l, r, goal):
            while l <= r:
                mid = l + (r - l)//2;
                if numbers[mid] == goal:
                    return mid;
                elif goal < numbers[mid]:
                    r = mid - 1;
                else:
                    l = mid + 1
            return -1;
            
        for i in range(len(numbers) - 1):
            loc = binarySearch(i + 1, len(numbers) - 1, target - numbers[i]);
            if loc != -1:
                return [i + 1, loc + 1]
# 我是弱智，有个更快的方法。。
# 因为已经排序了。。所以，用two pointer，然后一前一后跟踪就行了。。

#def twoSum(self, numbers: List[int], target: int) -> List[int]:
#    first=0
#    last=len(numbers)-1
#    while first<last:
#        if numbers[first]+numbers[last]>target:
#            last=last-1
#        elif numbers[first]+numbers[last]<target:
#            first=first+1
#        else:
#            return [first+1,last+1]