import math
def square(side):
    P = side * 4
    S = side * side
    D = math.sqrt(2) * side
    t = (P,S,D)
    print(t)
square(5)