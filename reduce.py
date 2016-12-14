from printer import print_eq

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
		rem = []
		for polyR in right:
			found = 0
			for polyL in left:
				if polyR[1] == polyL[1] and not found:
					polyL[0] -= polyR[0]
					rem.append(polyR)
					found = 1
			if not found:
				polyR[0] *= -1
				left.append(polyR)
				rem.append(polyR)
		for a in rem:
			right.remove(a)
	rem = []
	for polyL in left:
		if polyL[1] == 0:
			polyL[0] *= -1
			right.append(polyL)
			rem.append(polyL)
		elif polyL[0] == 0 and polyL in left:
			rem.append(polyL)
	for a in rem:
		left.remove(a)
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
	return maximum - minimum

def reduce_eq(equation):
	simplify(equation)
	one_side(equation)
	maximum = simplify(equation)
	print "Polynomial Degree:", int(maximum)
	return int(maximum)
