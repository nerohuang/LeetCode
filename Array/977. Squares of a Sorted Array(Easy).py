class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted(num * num for num in A)

