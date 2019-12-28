class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        result = []
        min_max = 0
        for i in range(len(numbers)):
            if numbers[i] > target:
                min_max = i
                break
            if i + 1 == len(numbers):
                min_max = len(numbers) - 1
        print(min_max)
        for i in range(min_max):
            for j in range(i, min_max):
                print(min_max - i, min_max - j - 1)
                print(numbers[min_max - i], numbers[min_max - j - 1])
                if numbers[min_max - i] + numbers[min_max - j - 1] == target:
                    result.append(min_max - j)
                    result.append(min_max - i + 1)
                    result.sort()
                    return result