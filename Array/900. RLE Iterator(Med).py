class RLEIterator:

    def __init__(self, A: List[int]):
        self.count = [];
        self.number = [];
        for i in range(len(A)):
            if i % 2 == 0:
                self.count.append(A[i]);
            else:
                self.number.append(A[i]);
                
        
    def next(self, n: int) -> int:
        for idx in range(len(self.count)):
            if self.count[idx] >= n:
                self.count[idx] -= n;
                return self.number[idx];
            else:
                n -= self.count[idx]
                self.count[idx] = 0;
        return -1


#class RLEIterator:
#
#    def __init__(self, A: List[int]):
#        self.ptr = 0
#        self.A = A
#
#    def next(self, n: int) -> int:
#        while n:
#            if self.ptr >= len(self.A): return -1
#            while self.A[self.ptr] == 0:
#                self.ptr += 2
#                if self.ptr >= len(self.A):
#                    return -1
#            m = min(self.A[self.ptr], n)
#            n -= m
#            self.A[self.ptr] -= m
#        return self.A[self.ptr + 1]