class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        
        mp, ans = collections.defaultdict(list), 0
        for k, v in reservedSeats:
            mp[k - 1].append(v - 1)
        
        ans = (n - len(mp.keys())) * 2

        for k, v in mp.items():
            arr = [0] * 10
            for j in v:
                arr[j] = 1
            if not any(arr[1:5]): 
                ans += 1
                arr[1:5] = [1, 1, 1, 1]
            if not any(arr[3:7]): 
                ans += 1
                arr[3:7] = [1, 1, 1, 1]
            if not any(arr[5:9]): 
                ans += 1
                arr[5:9] = [1, 1, 1, 1]
        
        return ans

#思路：
#大体思路没错，想复杂了
#其实能构成座位的只有[2,3,4,5], [4,5,6,7], [6,7,8,9];
#然后做一个map，记录下所有改行已定的坐位。
#再然后对比上面三种可能，只有有一种可能就把那种可能全部变为预定然后ans + 1；