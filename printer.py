def print_eq(equation):
	outstr = " + ".join(["%g * X^%d" % (poly[0], poly[1]) for poly in equation[0]])
	if not outstr:
		outstr = '0'
	outstr += " = "
	if len(equation[1]):
		outstr += "%g" % equation[1][0][0]
	else:
		outstr += "0"
	print "Reduced form: " + outstr.replace("+ -", "- ")
