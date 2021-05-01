class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0, 10:0, 20:0};
        if bills[0] > 5:
            return False;
        for bill in bills:
            if bill == 5:
                change[bill] += 1;
            elif bill == 10:
                if change[5] >= 1:
                    change[5] -= 1;
                    change[10] += 1;
                else:
                    return False
            else:
                if change[10] and change[5]:
                    change[10] -= 1;
                    change[5] -= 1;
                elif change[5] >= 3:
                    change[5] -= 3;
                else:
                    return False;
        
        return True

# 思路：
# 没什么好说的，就是模拟
# 有10找10没10找5