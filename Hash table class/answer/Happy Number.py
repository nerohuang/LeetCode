class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        curr = n
        while True:
            new = sum([int(d)**2 for d in str(curr)])
            if new == 1:
                return True
            elif new in seen:
                return False
            else:
                seen.add(new)
                curr = new