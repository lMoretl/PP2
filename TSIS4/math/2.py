import math
def area_of_trapezoid(height,base1,base2):
    area_of_triangles=(math.fabs(base1-base2)/2)*height
    area_of_square=base1*height
    return area_of_square + area_of_triangles
print(area_of_trapezoid(5,5,6))