import sys
from ft_math import baby_sqrt

def solve_zero(equation):
	if len(equation[0]) != 0 or len(equation[1]) > 1:
		print "Something went wrong in solve_error"
		sys.exit(0)
	print "The solution is:"
	if not equation[1] or equation[1][0][0] == 0:
		print "All Real Numbers"
	else:
		print "No Solution"


def solve_one(equation):
	print "The solution is:"
	if not equation[1]:
		print "0"
	else:
		print "%g" % (equation[1][0][0] / equation[0][0][0])

def solve_two(equation):
	#assuming it's sorted (bx^1 + ax^2 = cx^0)
	a = equation[0][1][0]
	b = equation[0][0][0]
	c = equation[1][0][0] * -1
	if (b * b - 4 * a * c) < 0:
		print "No Real Solutions"
		sys.exit(0)
	x1 = (-b + baby_sqrt(b * b - 4 * a * c)) / (2 * a)
	x2 = (-b - baby_sqrt(b * b - 4 * a * c)) / (2 * a)
	print "Discriminant is strictly positive, the two solutions are:"
	print "%g" % x1
	print "%g" % x2
