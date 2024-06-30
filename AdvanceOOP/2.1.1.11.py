# Scenario
# Extend the class implementation prepared in the previous lab to support the addition and subtraction of integers to time interval objects;
# to add an integer to a time interval object means to add seconds;
# to subtract an integer from a time interval object means to remove seconds.


class TimeInterval:
    def __init__(self , hours , minutes , seconds):
        
        if not all(isinstance(i, int) for i in [hours, minutes, seconds]):
            raise TypeError("Hours, minutes, and seconds must be integers")
            
        self.seconds = seconds % 60
        extra_minutes = seconds // 60
        self.minutes = (minutes + extra_minutes) % 60
        extra_hours = (minutes + extra_minutes) // 60
        self.hours = hours + extra_hours
        
    def __str__(self):
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"
        
    
    def __add__(self, value):
        if not isinstance(value, int):
            raise TypeError("Can only add TimeInterval by an integer")
            
        total_seconds = self.to_seconds() + value
        return self.from_seconds(total_seconds)
        
    def __sub__(self , value):
        if not isinstance(value, int):
            raise TypeError("Can only sub TimeInterval by an integer")
            
        total_seconds = self.to_seconds() - value
        return self.from_seconds(total_seconds)
    
    def to_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    #使用 @classmethod 装饰器将 from_seconds 方法定义为类方法
    # 并将第一个参数命名为 cls。表示cls是类本身
    @classmethod
    def from_seconds(cls, total_seconds):
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return cls(hours, minutes, seconds)
        

interval1 = TimeInterval(hours=21, minutes=58, seconds=50)
value = 62

print(interval1) 
print(value) 

interval3 = interval1 + value
print(interval3) 

interval4 = interval1 - value
print(interval4) 


        
        