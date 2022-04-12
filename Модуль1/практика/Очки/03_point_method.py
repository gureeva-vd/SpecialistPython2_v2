#задача 2
points = [Point(3, 8), Point(7, -5), Point(10, -2), Point(0, 6), Point(-12, 0)]
random_point = Point(-12, 10)

for i in points:
    print (distance (i, random_point))


#задача 3
point1 = Point(2, 4)
point2 = Point(5, -2)

met_dist = point1.dist_to(point2)
print(f"Расстояние между точками = {met_dist}")

#задача 4
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

point_start = Point(0, 0)
list_ = []
for t in points:
    list_.append((distance(t, point_start)))

print(list_)

print(f'Координаты наиболее удаленной точки =  {max(list_)}')
