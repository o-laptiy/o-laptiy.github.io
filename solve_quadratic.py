import math

def solve_quadratic(a, b, c):
   d = (b * b) - (4 * a * c)
   if (d < 0):
      return None
   x1 = (-b + math.sqrt(d)) / 2
   x2 = (-b - math.sqrt(d)) / 2
   if (d > 0):
      return (x1, x2)
   elif (d == 0):
      return (x1)
solve_quadratic(1, -5, 6)
solve_quadratic(1,4,4)
solve_quadratic(1,0,1)
