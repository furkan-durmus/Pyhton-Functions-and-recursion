# Given four real numbers representing cartesian coordinates: (x1,y1),(x2,y2).
# Write a function distance(x1, y1, x2, y2) to compute the distance between the points (x1,y1) and (x2,y2).
# Read four real numbers and print the resulting distance calculated by the function.
# The formula for distance between two points can be found at Wolfram.

def distance(*a):
    return (((a[2]-a[0])**2)+((a[3]-a[1]))**2)**(1/2)
print(distance(float(input()),float(input()),float(input()),float(input())))