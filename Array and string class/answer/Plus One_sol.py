class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        length = len(digits)
        
        i = length - 1
        c = 1
        while (i >= 0):
            total = digits[i] + c
            if total >= 10:
                total -= 10
                digits[i] = total

            else:
                digits[i] = total
                return digits
            i-= 1

        digits.insert(0, c)
        
        return digits
                