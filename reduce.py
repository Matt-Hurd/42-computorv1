from printer import print_eq

def sort(equation):
	#later I guess
	pass

def one_side(equation):
	for side in equation:
		for x in range(len(side)):
			for y in range(len(side)):
				if (x != y):
					if (side[x][1] == side[y][1]):
						side[x][0] += side[y][0]
						side[y][0] = 0
	for side in equation:
		for x in side:
			if x[0] == 0:
				side.remove(x)
	left, right = equation
	while len(right):
		for polyR in right:
			found = 0
			for polyL in left:
				if polyR[1] == polyL[1]:
					polyL[0] -= polyR[0]
					right.remove(polyR)
					found = 1
			if not found:
				polyR[0] *= -1
				left.append(polyR)
				right.remove(polyR)
	for polyL in left:
		if polyL[1] == 0:
			polyL[0] *= -1
			right.append(polyL)
			left.remove(polyL)
		if polyL[0] == 0:
			left.remove(polyL)
	sort(equation)
	print_eq(equation)

def simplify(equation):
	minimum = 3
	maximum = 0
	for side in equation:
		for poly in side:
			if (len(poly) == 2):
				if (poly[1] < minimum):
					minimum = poly[1]
				if (poly[1] > maximum):
					maximum = poly[1]
			else:
				minimum = 0
				poly.append(0)
	for side in equation:
		for poly in side:
			poly[1] -= minimum
	return maximum

def reduce_eq(equation):
	simplify(equation)
	one_side(equation)
	maximum = simplify(equation)
	print "Polynomial Degree:", int(maximum)
	if int(maximum) > 2:
		print "The polynomial degree is stricly greater than 2, I can't solve."
		sys.exit(0)
	return int(maximum)
