class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        ans = triangle[-1];
        for layer in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[layer])):
                ans[i] = min(ans[i], ans[i + 1]) + triangle[layer][i];
        return ans[0]

"""
'Bottom-up' DP, on the other hand, is very straightforward: we start from the nodes on the bottom row; the min pathsums for 
these nodes are the values of the nodes themselves. From there, the min pathsum at the ith node on the kth row would be the 
lesser of the pathsums of its two children plus the value of itself, i.e.:

minpath[k][i] = min( minpath[k+1][i], minpath[k+1][i+1]) + triangle[k][i];
Or even better, since the row minpath[k+1] would be useless after minpath[k] is computed, we can simply set minpath as a 1D 
array, and iteratively update itself:

For the kth level:
minpath[i] = min( minpath[i], minpath[i+1]) + triangle[k][i]; 
"""