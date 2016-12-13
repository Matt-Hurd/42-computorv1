#!/usr/bin/python
from parser import parser
from reduce import reduce_eq
from solver import solve_zero, solve_one, solve_two

def computor():
	equation = parser()
	print equation
	degree = reduce_eq(equation)
	if degree == 0:
		solve_zero(equation)
	elif degree == 1:
		solve_one(equation)
	elif degree == 2:
		solve_two(equation)
	else:
		print "Something went terribly wrong"

if __name__ == "__main__":
    computor()
