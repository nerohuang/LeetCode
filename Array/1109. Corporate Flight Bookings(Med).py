class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        flight = {};
        for begin, end, book in bookings:
            for i in range(begin, end + 1):
                if i not in flight:
                    flight[i] = book;
                else:
                    flight[i] += book;
        ans = [0] * n;
        for i in range(1, n + 1):
            if i in flight:
                ans[i - 1] = flight[i];
        return ans;

#尼玛超时

#def corpFlightBookings(self, bookings, n):
#    res = [0] * (n + 1)
#    for i, j, k in bookings:
#        res[i - 1] += k
#        res[j] -= k
#    for i in xrange(1, n):
#        res[i] += res[i - 1]
#    return res[:-1]

#思路是累加，先把开始的飞机号加上预定人数，然后结束的飞机号减去预定人数为之后的累计做准备
#然后循环就行。。。