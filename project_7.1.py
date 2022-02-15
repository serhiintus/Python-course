import math 

class Sphere:
    def __init__(self, rad = 1.0, x = 0.0, y = 0.0, z = 0.0):
        self.radius = rad
        self.x = x
        self.y = y
        self.z = z
    def get_volume(self):
        return 4.0/3.0*math.pi*self.radius**3
    def get_square(self):
        return 4.0*math.pi*self.radius**2
    def get_radius(self):
        return self.radius
    def get_center(self):
        coordinates = (self.x, self.y, self.z)
        return coordinates
    def set_radius(self, r):
        self.radius = r
    def set_center(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
    def is_point_inside(self, a, b, c):
        if (a - self.x)**2 + (b - self.y)**2 + (c - self.z)**2 > self.radius**2:
            return False
        return True


s1 = Sphere()
print(s1.get_volume())
print(s1.get_square())
print(s1.is_point_inside(0, 0.99, 0))
print(s1.is_point_inside(0.99, 0, 0))
print(s1.is_point_inside(0, 0, 0.99))
s1.set_center(0.5, 1, 0)
s1.set_radius(1.1)
print(s1.is_point_inside(0, 0.99, 0))
print(s1.is_point_inside(0.99, 0, 0))
print(s1.is_point_inside(0, 0, 0.99))
#s0 = Sphere(0.5)
#print(s0.get_center())
#print(s0.get_volume())
#print(s0.is_point_inside(0, -1.5, 0))
#s0.set_radius(1.6)
#print(s0.is_point_inside(0, -1.5, 0))
#print(s0.get_radius())