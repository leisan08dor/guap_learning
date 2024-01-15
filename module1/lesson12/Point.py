class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return f'Point: x={self.x}, y={self.y}'   
    def __add__(self,other_point):
        return Section(self,other_point)
class Section:
    def __init__(self,point1,point2):
        self.point1=point1
        self.point2=point2
    def __str__(self):
        return f'{self.point1} {self.point2}'

point1=Point(1,1)
point2=Point(2,2)
section=point1+point2
print(type(section),section)

#эллипс как переопределить?