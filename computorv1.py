import sys
from math import sqrt

def test(a1, a2):
        """
                This section is a comment
                This function print some stuff
        """
        print(a1, a2)

def resolve_simple(arg):
	equa = arg.split('=')
	equa = equa[0].split(' ')
	a = equa[0].replace('x', '')
	if a == '':
		a = '1'
	if a == '-':
		a = '-1'
	a = float(a)
	b = equa[2]
	b = float(b)
	b = b * -1 if equa[1] == '-' else b
	result = b * -1 / a
	print(float(result))

def descriminant(a, b, c):
	des = b * b - 4 * a * c
	print(des)
	return des

def calculate_second(des, a, b, c):
	racine = sqrt(des)
	print(racine)
	print('\n')
	x1 = b * (-1)/(2*a)  + racine/(2*a)
	x2 = -b/(2*a) - racine/(2*a)
	print(x1)
	print(x2)
	x1 = (-b + des**0.5) / (2*a)
	x2 = (-b - sqrt(des)) / (2*a)
	# x1 = (-b + sqrt(des)) / (2*a)
	# x2 = (-b - sqrt(des)) / (2*a)
	print(x1)
	print(x2)

def calculate_premier(des, a, b, c):
	x = -b / (2*a)
	print(x)

if __name__ == '__main__':
        # resolve_simple(sys.argv[1])
		a = float(sys.argv[1])
		b = float(sys.argv[2])
		c = float(sys.argv[3])
		des = descriminant(a, b, c)
		if des > 0 :
			calculate_second(des, a, b, c)
		if des < 0:
			print('No solution\n')
		if des == 0:
			print('1 degre bitch\n')
			calculate_premier(des, a, b, c)
