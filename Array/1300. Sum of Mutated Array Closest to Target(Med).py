class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        if sum(arr) <= target:
            return max(arr);
        arr.sort();
        while arr and target >= arr[0] * len(arr):
            target -= arr.pop(0)
        return (int(round((target - 0.0001)/len(arr))))

#因为题目找的是最小的数，所以如果本来加起来就小于等于target的话只要是当前数组最大的就可以了
#如果不是，那么排序之后从小到大找到数组中某个数乘以个数是最接近target的
#当然，因为从最小开始，所以如果最小的那个数乘以len(arr)之后比target还小，那么去掉他，继续找
#直到找到某个数的出来结果比处理后的target大为止，然后target除以当前个数就能得出。
#为什么要减去0.0001是为了防止某些数字相除结果大于0.5往上取整，所以要扣掉0.0001