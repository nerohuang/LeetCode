class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[0] == 9:
            digits.insert(0, 0)
        l = len(digits) - 1
        next_plus = False
        if digits[l] == 9:
            next_plus = True
        for i in range(len(digits)):
            if next_plus:
                if digits[l - i] == 9:
                    digits[l - i] = 0
                    next_plus = True
                else:
                    digits[l - i] = digits[l - i] + 1
                    next_plus = False
                    break
            else:
                digits[l - i] = digits[l - i] + 1
                break
        if digits[0] == 0:
            digits.pop(0)
        return digits