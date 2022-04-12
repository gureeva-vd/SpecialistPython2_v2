#задача 4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist_to(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

point_start = Point(0, 0)
list_ = []
for t in points:
    list_.append((distance(t, point_start)))

print(list_)

print(f'Координаты наиболее удаленной точки =  {max(list_)}')

