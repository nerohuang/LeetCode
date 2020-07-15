class Solution(object):
	def threeSum(self, nums):
		res = []
		nums.sort()
		length = len(nums)
		for i in range(length-2): #[8]
			if nums[i]>0: break #[7]
			if i>0 and nums[i]==nums[i-1]: continue #[1]

			l, r = i+1, length-1 #[2]
			while l<r:
				total = nums[i]+nums[l]+nums[r]

				if total<0: #[3]
					l+=1
				elif total>0: #[4]
					r-=1
				else: #[5]
					res.append([nums[i], nums[l], nums[r]])
					while l<r and nums[l]==nums[l+1]: #[6]
						l+=1
					while l<r and nums[r]==nums[r-1]: #[6]
						r-=1
					l+=1
					r-=1
		return res

#First, we sort the array, so we can easily move i around and know how to adjust l and r.
#If the number is the same as the number before, we have used it as target already, continue. [1]
#We always start the left pointer from i+1 because the combination of 0~i has already been tried. [2]
#
#Now we calculate the total:
#If the total is less than zero, we need it to be larger, so we move the left pointer. [3]
#If the total is greater than zero, we need it to be smaller, so we move the right pointer. [4]
#If the total is zero, bingo! [5]
#We need to move the left and right pointers to the next different numbers, so we do not get repeating result. [6]
#
#We do not need to consider i after nums[i]>0, since sum of 3 positive will be always greater than zero. [7]
#We do not need to try the last two, since there are no rooms for l and r pointers.
#You can think of it as The last two have been tried by all others. [8]


#class Solution:
#    def threeSum(self,n):
#        f={}
#        #counter
#        for i in n:
#            f[i]=f.get(i,0)+1
#        n=sorted(f)
#        # print(f)
#        a=[]
#        for i,I in enumerate(n):
#            if not I: #I=0
#                if f[I]>2:a.append((0,0,0))
#            elif f[I]>1 and -2*I in f:
#                a.append((I,I,-2*I))    
#            if I<0:
#                t=-I
#                # print(n,t-n[-1],i+1)   
#                l=bisect_left(n,t-n[-1],i+1) #list; value; starting p for list,default=0
#                r=bisect_right(n,t//2,l)
#                # print(l,r)
#                for J in n[l:r]:
#                    K=t-J
#                    # print("t,JandK ",t, J,K)
#                    if K in f and K!=J:
#                        a.append((I,J,K))
#        return a