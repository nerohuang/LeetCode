class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # The length of the input array 
        length = len(nums)
        
        # The answer array to be returned
        answer = [0]*length
        
        # answer[i] contains the product of all the elements to the left
        # Note: for the element at index '0', there are no elements to the left,
        # so the answer[0] would be 1
        answer[0] = 1
        for i in range(1, length):
            
            # answer[i - 1] already contains the product of elements to the left of 'i - 1'
            # Simply multiplying it with nums[i - 1] would give the product of all 
            # elements to the left of index 'i'
            answer[i] = nums[i - 1] * answer[i - 1]
        
        # R contains the product of all the elements to the right
        # Note: for the element at index 'length - 1', there are no elements to the right,
        # so the R would be 1
        R = 1;
        for i in reversed(range(length)):
            
            # For the index 'i', R would contain the 
            # product of all elements to the right. We update R accordingly
            answer[i] = answer[i] * R
            R *= nums[i]
        
        return answer

#Algorithm

#1. Initialize two empty arrays, L and R where for a given index i, L[i] would contain the product of all the 
#numbers to the left of i and R[i] would contain the product of all the numbers to the right of i.
#2. We would need two different loops to fill in values for the two arrays. For the array L, L[0]L[0] would be 
#1 since there are no elements to the left of the first element. For the rest of the elements, we simply use 
#L[i] = L[i - 1] * nums[i - 1]L[i]=L[i−1]∗nums[i−1]. Remember that L[i] represents product of all the elements 
#to the left of element at index i.
#3. For the other array, we do the same thing but in reverse i.e. we start with the initial value of 1 in 
#R[length - 1]R[length−1] where lengthlength is the number of elements in the array, and keep updating R[i] in 
#reverse. Essentially, R[i] = R[i + 1] * nums[i + 1]R[i]=R[i+1]∗nums[i+1]. Remember that R[i] represents product
#of all the elements to the right of element at index i.
#4. Once we have the two arrays set up properly, we simply iterate over the input array one element at a time, and 
#for each element at index i, we find the product except self as L[i] * R[i]L[i]∗R[i].

# 0            1       2        3
# =================================
# 1,           2,      6,       24
# 1,          1*2    1*2*3   1*2*3*4
# =====================================
# 1*2*3*4    2*3*4    3*4       4
# 24,          24,     12,      4

# [i] = A[0]->[i-1] * B[i+1]->[n] 
# 24, 12, 8, 6

#class Solution:
#    def productExceptSelf(self, nums: List[int]) -> List[int]:
#        product = 1
#        zeros = 0
#        for n in nums:
#            if n != 0:
#                product = product * n
#            else:
#                zeros += 1
#        res = [0] * len(nums)
#        print(product, zeros)
#        for idx, n in enumerate(nums):
#            if n != 0:
#                res[idx] = product // n if zeros == 0 else 0
#            else:
#                res[idx] = product if zeros == 1 else 0
#        return res