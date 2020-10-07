class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        minSum = threshold * k;
        ans = 0;
        
        nowSum = sum(arr[:k]);
        for i in range(k, len(arr)):
            if nowSum >= minSum:
                ans += 1;
            nowSum = nowSum + arr[i] - arr[i - k];
            
        if nowSum >= minSum:
            ans += 1;
        
        return ans;

#思路 : slid windows