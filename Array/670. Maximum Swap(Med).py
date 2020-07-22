class Solution:
    def maximumSwap(self, num: int) -> int:
        strNum = str(num);
        singleNum =[];
        for number in strNum:
            singleNum.append(int(number));
        maxNum = max(singleNum);
        for i in range(len(singleNum)):
            if singleNum[i] != max(singleNum[i:]):
                revers = singleNum[i:]
                maxIdx = revers[::-1].index(max(singleNum[i:]));
                singleNum[i], singleNum[len(singleNum) - 1 - maxIdx] = singleNum[len(singleNum) - 1 - maxIdx], singleNum[i];
                break;
        strAns = '';
        for number in singleNum:
            strAns += str(number);
        return int(strAns);


#from collections import deque
#from typing import List
#class Solution:
#    def maximumSwap(self, num: int) -> int:
#        # need to take care of 0?
#        # break num into array of digits
#        digits = deque()
#        while num :
#            digits.appendleft(num % 10)
#            num = num // 10
#        # build a counter array
#        counter = [0]* 10 # 0-9
#        for digit in digits:
#            counter[digit] += 1
#        # 
#        for i, digit in enumerate(digits):
#            largest = self.get_largest(counter)
#            if digit == largest:
#                counter[largest] -= 1
#            else:
#                j = self.find_largest_from_right(largest, digits)
#                digits[i], digits[j] = digits[j], digits[i]
#                return self.get_num(digits)
#        return self.get_num(digits) # No swap
#                
#
#     
#    # O(10)
#    def get_largest(self, counter: List[int]):
#        for i in range(len(counter)-1, -1, -1):
#            if counter[i] > 0:
#                return i
#    # O(n) 
#    def find_largest_from_right(self, largest, digits):
#        for i in range(len(digits)-1, -1, -1):
#            if digits[i] == largest:
#                return i
#            
#    def get_num(self, digits):
#        num = 0
#        for digit in digits:
#            num = num * 10 + digit
#        return num   
