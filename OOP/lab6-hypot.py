import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        
        self._x = float(x)
        self._y = float(y)

    def getx(self):
        return self._x

    def gety(self):
        return self._y
        
    def distance_from_xy(self, x, y):
        dis = math.hypot(self._x - x , self._y - y)
        return dis

    def distance_from_point(self, point):
        dis = math.hypot(self._x - point.getx() , self._y - point.gety())
        return dis


point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
