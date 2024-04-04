
import calendar

class MyCalendar(calendar.Calendar):
    # 执行父类的构造函数
    # 以便初始化从父类继承的任何属性或方法。
    #def __init__(self):
        #super().__init__()

    def count_weekday_in_year(self, year, weekday):
        if weekday < 0 or weekday > 6:
            raise ValueError("Weekday parameter must be between 0 and 6")

        total_count = 0
        for month in range(1, 13):
            for week in self.monthdays2calendar(year, month):
                for day, wkd in week:
                    if wkd == weekday and day != 0:
                        total_count += 1
        return total_count


my_calendar = MyCalendar()
year = 2019
weekday = 0  # Monday
count = my_calendar.count_weekday_in_year(year, weekday)
print(f"Number of Mondays in {year}: {count}")


