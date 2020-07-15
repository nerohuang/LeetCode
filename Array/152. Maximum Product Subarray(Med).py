#class Solution:
#    def maxProduct(self, A):
#        B = A[::-1]
#        for i in range(1, len(A)):
#            A[i] *= A[i - 1] or 1
#            B[i] *= B[i - 1] or 1
#        return max(A + B)
#
#It's actually a variant of Kadane's algorithm.
#Detailed Explanation:
#A lot of people asked about why can we get the max by calculating the products from start and end, Here is all you should know:
#First, Consider there is no zero, and if we get the products of all the numbers:
#1) We will have a negative result if there are odd numbers of negative -> max ((product of (0, last negative)), (product of (first negative, last num))
#2) We will have a positive result if there are even numbers of negative -> product of all the numbers
#Above all, we can get the max by going through the array from both start and end, then we won't miss any situations
#If there is a zero, that means we would have two subproblems(unless the zero is at index 0 or last index), if two zeros, 3 subs, 
#all the way up. We still can calculate from the very beginning and end at the same time, then we would get the result.



#class Solution:
#    def maxProduct(self, nums):
#        if len(nums) == 0:
#            return 0
#        maxx = minx = res = nums[0]
#        for x in nums[1:]:
#            maxx, minx = max(x, maxx*x, minx*x),min(x, maxx*x, minx*x)
#            res = max(res, maxx)
#        return res