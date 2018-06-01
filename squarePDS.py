"""This program is calculating perimeter, area and diagonal of a square"""
import math
def square(side):
    P = side * 4
    A = side * side
    D = math.sqrt(2) * side
    t = (P,S,D)
    print(t)
print("Enter the side of square")
side = float(input())
square(5)