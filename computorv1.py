#!/usr/bin/python
from parser import parser
from reduce import reduce_eq
from solver import solve_zero, solve_one, solve_two
import sys

def computor(instr):
	equation = parser(instr)
	if not equation:
		return ;
	degree = reduce_eq(equation)
	if degree > 2:
		print "The polynomial degree is stricly greater than 2, I can't solve."
		return ;
	if degree == 0:
		solve_zero(equation)
	elif degree == 1:
		solve_one(equation)
	elif degree == 2:
		solve_two(equation)
	else:
		print "Something went terribly wrong"

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Invalid number of arguments"
		sys.exit(0)
	computor(sys.argv[1])
