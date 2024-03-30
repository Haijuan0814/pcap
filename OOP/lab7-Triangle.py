import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x
        

    def gety(self):
        return self.__y
        

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x , self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())



class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        
        self.x = float(vertice1.distance_from_point(vertice2))
        self.y = float(vertice1.distance_from_point(vertice3))
        self.z = float(vertice3.distance_from_point(vertice2))

    def perimeter(self):
        return (self.x + self.y + self.z) 


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
