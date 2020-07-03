class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort();
        result = [];
        curMin = 0;
        lastMin = arr[1] - arr[0];
        for i in range(len(arr) - 1):
            curMin = arr[i + 1] - arr[i];
            if curMin == lastMin:
                result.append([arr[i], arr[i + 1]]);
            else:
                if lastMin > curMin:
                    result = [];
                    lastMin = curMin;
                    result.append([arr[i], arr[i + 1]]);
        return result;


##class Solution:
##    def minimumAbsDifference(self,arr:List[int])->List[List[int]]:
##
##        
##r,m,s=[],999999,sorted(arr)
##print(list(zip(s,s[1:])))
##for a,b in zip(s,s[1:]):
##    d=b-a;
##    if m>d:
##        m,r=d,[[a,b]];
##    elif m==d:
##        r.append([a,b]);
##print(r)