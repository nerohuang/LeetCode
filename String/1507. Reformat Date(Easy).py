class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan" : "01",
                 "Feb" : "02",
                 "Mar" : "03",
                 "Apr" : "04",
                 "May" : "05",
                 "Jun" : "06",
                 "Jul" : "07",
                 "Aug" : "08",
                 "Sep" : "09",
                 "Oct" : "10",
                 "Nov" : "11",
                 "Dec" : "12"}
        
        dates = date.split(" ");
        day = dates[0][:-2];
        if len(day) < 2:
            day = "0" + day;
        ans = dates[2] + "-" + month[dates[1]] + "-" + day;
        return ans