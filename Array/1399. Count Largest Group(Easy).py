class Solution:
    def countLargestGroup(self, n: int) -> int:
        def countDigits(num):
            numString = str(num);
            result = 0;
            for di in numString:
                result += int(di);
            return (result);
        
        store = {};
        for i in range(1, n + 1):
            digitSum = countDigits(i);
            if digitSum not in store:
                store[digitSum] = 1;
            else:
                store[digitSum] += 1;
        largestSize = (max(store.values()));
        ans = 0;
        for value in store.values():
            if largestSize == value:
                ans += 1;
        return ans;

##class Solution:
##    def countLargestGroup(self, n: int) -> int:
##        
##        from collections import defaultdict
##        
##        digit_sums = defaultdict(list)
##        digit_sums[1].append(1)
##        cur_sum = 1
##        for i in range(2,n+1):
##            if i % 10 != 0:
##                cur_sum += 1
##                digit_sums[cur_sum].append(i)
##            else:
##                zeros = 0 
##                while i % 10 == 0:
##                    zeros += 1
##                    i = i//10
##                cur_sum = cur_sum + 1 - 9*zeros
##                digit_sums[cur_sum].append(i)
##        
##        largest_size = max([len(l) for l in digit_sums.values()])
##        count = 0
##        for key in digit_sums.keys():
##            if len(digit_sums[key]) == largest_size:
##                count += 1
##        
##        return count