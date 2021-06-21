class MyCalendar:

    def __init__(self):
        
        self.calendar = [];

    def book(self, start: int, end: int) -> bool:
        if self.calendar == []:
            self.calendar.append([start, end]);
            return True;
        else:
            for begin, last in self.calendar:
                if end > begin and last > start:
                    return False;
        self.calendar.append([start, end]);
        return True;


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)

# return True :
# end <= 已有的start or start => 已有的end
# return false:
# end > 已有的start or start < 已有的end

# 我们将维护一个日程安排列表（不一定要排序）。当且仅当其中一个日程
# 安排在另一个日程安排结束后开始时，两个日程安排 [s1，e1) 和 [s2，e2) 
# 不冲突：e1<=s2 或 e2<=s1。这意味着当 s1<e2 和 s2<e1 时，日程安排发生冲突。



#class MyCalendar:
#
#    def __init__(self):
#        self.start = []
#        self.toend = {}
#
#    def book(self, start: int, end: int) -> bool:
#        pos = bisect.bisect_left(self.start, start)
#        if pos > 0 and self.toend[self.start[pos-1]] > start:
#            return False
#        if pos < len(self.start) and self.start[pos] < end:
#            return False
#        self.toend[start] = end
#        self.start.insert(pos, start)
#        # bisect.insort_left(self.start, start)
#        return True
#    
#
#
## Your MyCalendar object will be instantiated and called as such:
## obj = MyCalendar()
## param_1 = obj.book(start,end)
