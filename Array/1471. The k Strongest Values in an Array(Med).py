class Solution:
    def getStrongest(self, arr: List[int], k: int) -> List[int]:
        arr.sort();
        median = arr[(len(arr) - 1)//2];
        
        i, j = 0, len(arr) - 1;
        ans = [];
        while i <= j and k:
            if abs(arr[i] - median) > abs(arr[j] - median):
                ans.append(arr[i]);
                i += 1;
            else:
                ans.append(arr[j]);
                j -= 1;
            k -= 1;
            
        return ans

#思路：
#先sort然后求出median
#然后他所指定的规则：
#abs(arr[i] - median) > abs(arr[j] - median)
#其实就摆明了离median越远越strong，所以就从最左和最右开始往里收拢
#又因为规则问题，当最左边的最左边的arr[i]用第一个规则不比最右边的arr[j]
#大的时候，那么按照第二个规则，就加入arr[j]，因为数组从小到大排列
#arr[j]数值上绝对大于等于arr[i]