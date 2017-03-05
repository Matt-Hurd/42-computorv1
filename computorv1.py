#!/usr/bin/python
from parser import parser
from reduce import reduce_eq
from solver import solve_zero, solve_one, solve_two
import sys

def computor(instr, derivative=False, disc=False):
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

def test():
	strs = [
	"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
	"5 * X^0 + 4 * X^1 = 4 * X^0",
	"8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
	"5 + 4 * X + X^2= X^2",
	"5 * X ^ 0 = 5 * X ^ 0",
	"5 * X ^ 0 = 4 * X ^ 0 + 7 * X ^ 1",
	"5 * X ^ 0 + 13 * X ^ 1 + 3 * X ^ 2 = 1 * X ^ 0 + 1 * X ^ 1",
	"5 * X ^ 0 + 3 * X ^ 1 + 3 * X ^ 2 = 1 * X ^ 0 + 0 * X ^ 1"
	]
	for s in strs:
		print "Test input:", s
		computor(s)
		print ""

if __name__ == "__main__":
	if len(sys.argv) == 1:
		print "No args given, running tests"
		test()
		sys.exit(0)
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
