#!/usr/bin/python
from parser import parser
from reduce import reduce_eq
from solver import solve_zero, solve_one, solve_two
import sys

def computor(instr, derivative, disc=False):
	equation = parser(instr)
	if not equation:
		return ;
	degree = reduce_eq(equation, derivative)
	if degree > 2:
		print "The polynomial degree is stricly greater than 2, I can't solve."
		return ;
	if degree == 0:
		solve_zero(equation)
	elif degree == 1:
		solve_one(equation)
	elif degree == 2:
		solve_two(equation, disc)
	else:
		print "Something went terribly wrong"

def print_usage():
	print "usage: %s [-di] [expression]" % sys.argv[0]

if __name__ == "__main__":
	derivative = False
	discriminant = False
	if len(sys.argv) not in range(2,4):
		print "Invalid number of arguments"
		sys.exit(0)
	if len(sys.argv) == 3:
		if sys.argv[1][0] != '-':
			print_usage()
			sys.exit(0)
		if 'd' in sys.argv[1]:
			derivative = True
		if 'i' in sys.argv[1]:
			discriminant = True
	computor(sys.argv[-1], derivative, discriminant)
