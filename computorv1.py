import sys
import re
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

def found_puissance(str):
	"""Take a string X^x where x is integer and return this integer else
	return -1"""
	x = -1
	try:
		s = str.replace('X^', '')
		x = float(s)
	except:
		return -1
	return x

def is_infinite_solution(s):
	"""Take a string and check if the equation before and after '=' are the same
	"""
	try:
		tab = s.split('=')
		if tab[0].strip() == tab[1].strip():
			return 1
	except:
		return -1
	return 0

def decompose_right(s):
	"""Return a array with each elem before the '='"""
	tab = s.strip().split(' ')
	return tab

def decompose_left(s):
	tab = s.strip().split(' ')

	x = {}
	x['nb'] = float(tab[0])
	p = found_puissance(tab[2])
	x['str'] = tab[2]
	if p != -1:
		x['degre'] = p
	else:
		x['degre'] = 0
	return x

def calculate_reduced(tab, di, i, l):
	# TODO checker si c'est un double ou pas
	if i - 2 >= 0 and tab[i - 1] == '*':
		tab[i - 2] = float(tab[i - 2]) - di['nb']
		return tab
	if i + 2 < l and tab[i + 1] == '*':
		tab[i + 2] = float(tab[i + 2]) - di['nb']
		return tab
	return

def found_reduced_form(tab, di):
	l = len(tab)
	i = 0
	while i < l:
		if tab[i] == di['str']:
			tmp = calculate_reduced(tab, di, i, l)
			if tmp:
				return tmp
		i += 1
	return tab

def print_reduced(tab):
	s = 'Reduced form:'
	for t in tab:
		s += ' '
		s += str(t)
		# replace a enlever une fois que calculate_reduced TODO done
		s = s.replace('.0', '')
	s += ' = 0'
	print(s)

def replace_puissance(tab):
	l = len(tab)
	i = 0
	while i < l:
		if str(tab[i]) == 'X^0':
			tab[i] = 1
		if str(tab[i]) == 'X^1':
			tab[i] = 'X'
		i += 1
	return tab

if __name__ == '__main__':
		# resolve_simple(sys.argv[1])
		if is_infinite_solution(sys.argv[1]) == 1:
			print('0 = 0\nThe solution are infinite')
			sys.exit()
		# decompose(sys.argv[1])
		tab = sys.argv[1].strip().split('=')
		right = tab[0].strip()
		left = tab[1].strip()
		di_left = decompose_left(left)
		tab_right = decompose_right(right)
		print(di_left)
		print(tab_right)
		tab_reduced = found_reduced_form(tab_right, di_left)
		print(tab_reduced)
		print_reduced(tab_reduced)
		tab_reduced = replace_puissance(tab_reduced)
		print(tab_reduced)
		sys.exit()



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
