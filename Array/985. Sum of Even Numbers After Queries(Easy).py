class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sum = 0;
        for num in A:
            if num % 2 == 0:
                sum += num;
        result = [];
        for val, i in queries:
            if A[i] % 2 == 0:
                sum -= A[i];
            if (A[i] + val) % 2 == 0:
                A[i] += val;
                sum += A[i];
            else:
                A[i] += val;
            result.append(sum);
        return result;