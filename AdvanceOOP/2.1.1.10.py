# Scenario
# Create a class representing a time interval;
# the class should implement its own method for addition, subtraction on time interval class objects;
# the class should implement its own method for multiplication of time interval class objects by an integer-type value;
# the __init__ method should be based on keywords to allow accurate and convenient object initialization, but limit it to hours, minutes, and seconds parameters;
# the __str__ method should return an HH:MM:SS string, where HH represents hours, MM represents minutes and SS represents the seconds attributes of the time interval object;
# check the argument type, and in case of a mismatch, raise a TypeError exception.



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
        
    
    def __add__(self, other):
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval to TimeInterval")
        return TimeInterval(
            hours=self.hours + other.hours,
            minutes=self.minutes + other.minutes,
            seconds=self.seconds + other.seconds
        )
        
    def __sub__(self , other):
        
        if not isinstance(other, TimeInterval):
            raise TypeError("Can only add TimeInterval to TimeInterval")
        return TimeInterval(
            hours=self.hours + other.hours,
            minutes=self.minutes + other.minutes,
            seconds=self.seconds + other.seconds
        )
        
        total_seconds_self = self.hours * 3600 + self.minutes * 60 + self.seconds
        total_seconds_other = other.hours * 3600 + other.minutes * 60 + other.seconds
        total_seconds_result = total_seconds_self - total_seconds_other
        
        if total_seconds_result < 0:
            raise ValueError("Resulting TimeInterval cannot be negative")
        
        hours = total_seconds_result // 3600
        minutes = (total_seconds_result % 3600) // 60
        seconds = total_seconds_result % 60
        return TimeInterval(hours, minutes, seconds)
    
    def __mul__(self, value):
        if not isinstance(value, int):
            raise TypeError("Can only multiply TimeInterval by an integer")
        total_seconds = (self.hours * 3600 + self.minutes * 60 + self.seconds) * value
        if total_seconds < 0:
            raise ValueError("Resulting TimeInterval cannot be negative")
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        return TimeInterval(hours, minutes, seconds)
        

# Example usage:
interval1 = TimeInterval(hours=1, minutes=20, seconds=35)
interval2 = TimeInterval(hours=2, minutes=40, seconds=50)

print(interval1)  # 01:20:35
print(interval2)  # 02:40:50

interval3 = interval1 + interval2
print(interval3)  # 04:01:25

interval4 = interval2 - interval1
print(interval4)  # 01:20:15

interval5 = interval1 * 3
print(interval5)  # 04:01:45

        
        