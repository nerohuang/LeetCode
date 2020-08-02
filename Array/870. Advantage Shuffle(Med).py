import collections;
class Solution:
    def advantageCount(self, A, B):
        A = sorted(A)
        take = collections.defaultdict(list)
        for b in sorted(B)[::-1]:
            if b < A[-1]: take[b].append(A.pop())
        return [(take[b] or A).pop() for b in B]

#1.Sort A
#2.For every element b in B from big to small,
#if A[-1] > b, then this b will take A.pop()
#3.Assign all elements in B an element from take or the rest of A