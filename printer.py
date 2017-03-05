def print_eq(equation, derivative, d=False):
	outstr = ""
	if len(equation[1]):
		outstr += "%g" % (equation[1][0][0] * -1)
		if len(equation[0]):
			outstr += " + "
	outstr += " + ".join(["%g * X^%d" % (poly[0], poly[1]) for poly in equation[0]])
	if not outstr:
		outstr = '0'
	outstr += " = 0"
	if not d:
		print "Reduced form: " + outstr.replace("+ -", "- ")
	if d:
		print "Derivative: " + outstr.replace("+ -", "- ")
	if derivative:
		derived = []
		for x in equation[0]:
			new = x[:]
			new[1] -= 1
			if new[1] >= 0:
				derived.append(new)
		derived = (derived, [])
		print_eq(derived, False, True)
		# for eq in equation:
		# 	derivated +=
