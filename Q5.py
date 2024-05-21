import math

# Task 1: Calculate the area and circumference of a circle with radius 30 meters
radius = 30
_area_of_circle_ = math.pi * radius ** 2
_circum_of_circle_ = 2 * math.pi * radius

print(f"Area of the circle with radius 30 meters: {_area_of_circle_:.2f} square meters")
print(f"Circumference of the circle with radius 30 meters: {_circum_of_circle_:.2f} meters")

# Task 2: Take radius as user input and calculate the area
radius = float(input("Enter the radius of the circle (in meters): "))
area = math.pi * radius ** 2

print(f"Area of the circle with radius {radius} meters: {area:.2f} square meters")
