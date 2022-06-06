import math 
class Triangle():
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
	
	def perimeter(self):
		return self.a + self.b + self.c

	def area(self):
		s = (self.a + self.b + self.c) / 2
		return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

	def scale(self, scale_factor):
		return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)


	def is_valid(self):
		if((self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a)):
			return True

	def is_right(self):
		if(math.pow(self.a, 2) + math.pow(self.b, 2) == math.pow(self.c, 2) or 
			math.pow(self.b, 2) + math.pow(self.c, 2) == math.pow(self.a, 2) or 
			math.pow(self.a, 2) + math.pow(self.c, 2) == math.pow(self.b, 2)):
			return True

r = Triangle(3, 4, 5)

print("Area = %d" % r.area())

print("perimeter = %d" % r.perimeter())

print(r.is_valid())
print(r.is_right())

q = r.scale(2)

print(q.a, q.b, q.c)