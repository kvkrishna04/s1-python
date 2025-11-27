from graphics import rectangle, circle
from graphics.threee_d import cuboid, sphere

print("Rectangle area:", rectangle.area(15, 10))
print("Rectangle perimeter:", rectangle.parimeter(10, 5))

print("Circle area:", circle.area(7))
print("Circle perimeter:", circle.parimeter(7))

print("Cuboid surface area:", cuboid.area(4, 5, 6))
print("Cuboid volume:", cuboid.volume(4, 5, 6))

print("Sphere surface area:", sphere.area(5))
print("Sphere volume:", sphere.volume(5))
