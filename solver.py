# -*- coding: UTF-8 -*-
import sys
from ft_math import baby_sqrt

def solve_zero(equation):
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
	a = 0
	b = 0
	c = 0
	for side in equation:
		for poly in side:
			if len(poly) < 2 or poly[1] == 0:
				if len(poly) == 0:
					c = 0
				else:
					c = ((poly[0]) if (side == equation[0]) else (poly[0] * -1))
			elif poly[1] == 1:
				b = poly[0]
			elif poly[1] == 2:
				a = poly[0]
	inner = b * b - 4 * a * c
	if (inner) < 0:
		disc = baby_sqrt(-inner)
		print "The two complex solutions are:"
		print "%g ± %g𝓲" % (-b / (2 * a), disc / (2 * a))
	elif inner != 0:
		x1 = (-b + baby_sqrt(inner)) / (2 * a)
		x2 = (-b - baby_sqrt(inner)) / (2 * a)
		print "The two solutions are:"
		print "%g" % x1
		print "%g" % x2
	else:
		x = (-b + baby_sqrt(inner)) / (2 * a)
		print "Discriminant is 0, the two solution is:"
		print "%g" % x
