
import math

class point():
    x = 0
    y = 0
p1 = point()
p2 = point()
p1.x = 10
p1.y = 20
p2.x = 5
p2.y = 8
def distance_between_points (p1,p2):
    total = math.sqrt((p2.x-p1.x)**2+(p2.y-p1.y)**2)
    return total
print (distance_between_points(p1,p2))