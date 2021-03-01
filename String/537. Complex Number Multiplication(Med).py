class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        def getInt(num):
            nums = num.split('+');
            return int(nums[0]), int(nums[1][:-1]);
        
        intA1, intA2 = getInt(a);
        intB1, intB2 = getInt(b);
        ans = str(intA1*intB1 - intA2*intB2) + '+' + str(intA1*intB2 + intA2*intB1) + 'i';
        
        return ans