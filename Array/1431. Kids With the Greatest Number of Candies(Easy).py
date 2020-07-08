class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [];
        maxCandy = max(candies);
        for num in candies:
            if num + extraCandies >= maxCandy:
                result.append(True);
            else:
                result.append(False);
        return result;