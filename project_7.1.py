import math 

#class Sphere describe sphere in three-dimensional space
class Sphere:
    #constructor that takes 4 real numbers: radius, and 3 coordinates of the center of the sphere
    def __init__(self, rad = 1.0, x = 0.0, y = 0.0, z = 0.0):
        self.radius = rad
        self.x = x
        self.y = y
        self.z = z
    #this method returns a real number is the volume of a sphere bounded by the current sphere
    def get_volume(self):
        return 4.0/3.0*math.pi*self.radius**3
    #this method returns the real number - the area of the outer surface of the sphere
    def get_square(self):
        return 4.0*math.pi*self.radius**2
    #this method returns a real number is the radius of the sphere
    def get_radius(self):
        return self.radius
    #this method returns a tuple with 3 real numbers - the coordinates of the center of the sphere 
    #in the same order in which they are specified in the constructor
    def get_center(self):
        coordinates = (self.x, self.y, self.z)
        return coordinates
    #this method takes 1 argument is a real number and changes the radius of the current sphere without returning anything
    def set_radius(self, r):
        self.radius = r
    #this method takes 3 arguments - real numbers, and changes the coordinates of the center of the sphere without returning anything.
    #The coordinates are set in the same order as in the constructor
    def set_center(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
    #this method takes 3 arguments - real numbers - the coordinates of a point in space (in the same order as in the constructor)
    #and returns a logical value of True or False, depending on whether the point is inside the sphere
    def is_point_inside(self, a, b, c):
        if (a - self.x)**2 + (b - self.y)**2 + (c - self.z)**2 > self.radius**2:
            return False
        return True

#examples:
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
s0 = Sphere(0.5)
print(s0.get_center())
print(s0.get_volume())
print(s0.is_point_inside(0, -1.5, 0))
s0.set_radius(1.6)
print(s0.is_point_inside(0, -1.5, 0))
print(s0.get_radius())