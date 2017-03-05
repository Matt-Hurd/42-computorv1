import sys
import re

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
		if not s:
			arr.remove(s)
	try:
		ret = [[float(str_helper(i)) for i in x.split('x')] for x in arr]
	except:
		return 0
	return ret

def parser(instr):
	if instr.count("=") != 1:
		print "Invalid Number of Equal Signs"
		return 0
	instr = instr.replace(' ', '').replace('*', '')
	if not re.match(r"^(\d*.{0,1}\d*(X{0,1}(\^\d+){0,1}){0,1}[+=\-*]{0,1})+$", instr):
		print "Invalid input string"
		return 0
	split = instr.split('=')
	left = str_to_polys(split[0])
	right = str_to_polys(split[1])
	if not left or not right:
		print "Invalid equation"
		return 0
	return (left, right)
