import sys

def str_helper(instr):
	instr = instr.replace("^", '').replace('*', '')
	if (not instr):
		instr = '1'
	return instr

def str_to_polys(instr):
	arr = instr.replace(' ', '').lower().replace('-', '+-').split('+')
	for s in arr:
		if ('*' in s and not 'x' in s) or '/' in s:
			print "Operation Not Supported"
			sys.exit(0)
	ret = [[float(str_helper(i)) for i in x.split('x')] for x in arr]
	return ret

def parser():
	if len(sys.argv) != 2:
		print "Invalid number of arguments"
		sys.exit(0)
	inputstr = sys.argv[1]
	if len(inputstr.split('=')) != 2:
		print "Invalid equation"
		sys.exit(0)
	split = inputstr.split('=')
	left = str_to_polys(split[0])
	right = str_to_polys(split[1])
	return (left, right)
