class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        length = len(nums);
        ans = 0;        
        goThrough = set();
        for i in range(length):
            if nums[i] in goThrough:
                continue;
            count = 0;
            begin = nums[i];
            while True:
                begin = nums[begin];
                count += 1;
                goThrough.add(nums[begin]);
                if begin == nums[i]:
                    break;
            ans = max(ans, count);
            goThrough.add(nums[i])
        return(ans);

#Approach #2 Using Visited Array [Accepted]
#Algorithm
#
#In the last approach, we observed that in the worst case, all the elements 
# of the numsnums array are added to the sets corresponding to all the starting 
# indices. But, all these sets correspond to the same set of elements only, 
# leading to redundant calculations.
#
#We consider a simple example and see how this problem can be resolved. From the
#figure below, we can see that the elements in the current nesting shown by 
# arrows form a cycle. Thus, the same elements will be added to the current set 
# irrespective of the first element chosen to be added to the set out of these 
# marked elements.

#https://leetcode.com/problems/array-nesting/solution/

#class Solution:
#    def arrayNesting(self, nums: List[int]) -> int:
#        rst = 0
#        def count(start):
#            c = 0
#            while nums[start] >= 0:
#                ne = nums[start]
#                nums[start] = -1
#                start = ne
#                c += 1
#            return c
#        for i in range(len(nums)):
#            if nums[i] >= 0:
#                rst = max(rst, count(i))
#        
#        return rst