from computorv1 import computor
import random
import string

def test():
	while 1:
		instr = ''.join(random.SystemRandom().choice(string.digits + '+-=Xx^ ') for _ in range(int(random.random() * 10)))
		print instr
		computor(instr)

if __name__ == "__main__":
	test()
