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
