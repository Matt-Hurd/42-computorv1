# -*- coding: UTF-8 -*-
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
	inner = b * b - 4 * a * c
	if (inner) < 0:
		disc = baby_sqrt(-inner)
		print "Discriminant is negative, the two complex solutions are:"
		print "%g ± %g𝓲" % (-b / (2 * a), disc / (2 * a))
		sys.exit(0)
	elif inner != 0:
		x1 = (-b + baby_sqrt(inner)) / (2 * a)
		x2 = (-b - baby_sqrt(inner)) / (2 * a)
		print "Discriminant is strictly positive, the two solutions are:"
		print "%g" % x1
		print "%g" % x2
	else:
		x = (-b + baby_sqrt(inner)) / (2 * a)
		print "Discriminant is 0, the two solution is:"
		print "%g" % x
