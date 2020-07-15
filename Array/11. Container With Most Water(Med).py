class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = 0;
        l = 0;
        r = len(height) - 1;
        while l < r:
            result = max(result, min(height[l], height[r]) * (r - l));
            if (height[l] < height[r]):
                l += 1;
            else:
                r -= 1;
        return result;

#class Solution:
#    def maxArea(self, height: List[int]) -> int:
#        i=0
#        j=len(height)-1
#        max_area=0
#        while i<j:
#            if height[i]<height[j]:
#                area = (j-i)*height[i]
#                i+=1
#            else:
#                area = (j-i)*height[j]
#                j-=1
#                
#            max_area = max(max_area,area)
#            
#        return max_area