from datetime import date

class Solution:
    str_tbl = [
        "Monday", 
        "Tuesday", 
        "Wednesday", 
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return self.str_tbl[date(year, month, day).weekday()]