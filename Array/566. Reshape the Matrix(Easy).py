class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        newList = [];
        subList = [];
        if len([ele for sub in nums for ele in sub]) != r * c:
            return nums;
        else:
            for i in range(len(nums)):
                for j in range(len(nums[i])):
                    if len(subList) < c:
                        subList.append(nums[i][j]);
                    else:
                        newList.append(subList);
                        subList = [];
                        subList.append(nums[i][j]);
        newList.append(subList);
        return newList;


##class Solution:
##    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
##        m=len(nums)
##        n=len(nums[0])
##        if m*n!=r*c:
##            return nums
##        res=[]
##        cur=[]
##        i=0
##        while True:
##            while i<m and len(cur)<c:
##                cur.extend(nums[i])
##                i+=1
##            while len(cur)>=c:
##                row=cur[:c]
##                res.append(row)
##                cur=cur[c:]
##            if i==m:
##                break
##        return res