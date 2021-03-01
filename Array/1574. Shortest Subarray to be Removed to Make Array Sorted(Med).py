class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        j = len(arr) - 1;
        while(j > 0 and arr[j - 1] <= arr[j]):
            j -= 1;
        if j == 0:
            return 0;
        ans = j;
        for i in range(j):
            if(i > 0 and arr[i - 1] > arr[i]):
                break;
            while(j < len(arr) and arr[i] > arr [j]):
                j += 1;
            ans = min(ans, j - i - 1);
        
        return ans

#丢，subarray。。。
#思路是先找到最右边的下降位置j，比如
#arr = [1,2,3,10,4,2,3,5]的话
#就是arr[j] = 4，j = 4
#如果j=0就表示整个序列没有下降的，
#直接输出0；
#然后开始遍历到第j位开始
#然后让[0~i]位都是非递减的，这样就能得到
#[0~i], [j~n-1]能组成非递减的，所以去除
#[i+1 ~ j-1]就行了。
#但是如果发生arr[i]>arr[j]怎么办
#那么就把j往后推，一直推到
# arr[i]<=arr[j]就可以了。
#答案就是(j - i - 1).
