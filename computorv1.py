import sys
import re
# from math import sqrt

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
	return des

def calculate_simple(b, c):
	x = -c / b
	print("The solution is:\n" + str(x))

def calculate_premier(des, a, b, c):
	x = -b / (2*a)
	print('Discriminant is null, the solution is:')
	print(x)

def calculate_second(a, b, c):
	des = descriminant(a, b, c)
	if des < 0:
		print('No solution\n')
		return
	if des == 0:
		calculate_premier(des, a, b, c)
		return
	print('Discriminant is strictly positive, the two solutions are:')
	x1 = (-b + des**0.5) / (2*a)
	x2 = (-b - des**0.5) / (2*a)
	print(x1)
	print(x2)


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

def print_reduced_degre(tab):
	x = 0
	for v in tab:
		if isinstance(v, str) and re.match('X\^', v):
			tmp = v.replace('X^', '')
			tmp = int(tmp)
			if tmp > x:
				x = tmp
	s = 'Polynomial degree: ' + str(x)
	if x > 2:
		print("The polynomial degree is stricly greater than 2, I can't solve.")
		sys.exit()
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

def sort_puissance(tab):
	l = len(tab)
	i = 0
	while i < l:
		if tab[i] == '*':
			if re.match('X', str(tab[i - 1])) and re.match('X', str(tab[i + 1])) == None:
				tmp = tab[i - 1]
				tab[i - 1] = tab[i + 1]
				tab[i + 1] = tmp
				i = -1
		i += 1
	return tab

def cast_to_float(tab):
	l = len(tab)
	i = 0
	while i < l:
		try:
			tab[i] = float(tab[i])
		except:
			pass
		i += 1
	return tab

def replace_less(tab):
	l = len(tab)
	i = 0
	while i < l:
		try:
			if str(tab[i]) == '-':
				tab[i + 1] = tab[i + 1] * -1
				tab[i] = '+'
		except:
			pass
		i += 1
	return tab

def resolve_multi(tab):
	i = 0
	while i < len(tab):
		if str(tab[i]) == '*':
			if isinstance(tab[i - 1], float) and isinstance(tab[i + 1], float):
				tab[i] = tab[i - 1] * tab[i + 1]
				tab.pop(i - 1)
				tab.pop(i)
		i += 1
	return tab

def resolve_div(tab):
	i = 0
	while i < len(tab):
		if str(tab[i]) == '/':
			if isinstance(tab[i - 1], float) and isinstance(tab[i + 1], float):
				tab[i] = tab[i - 1] / tab[i + 1]
				tab.pop(i - 1)
				tab.pop(i)
		i += 1
	return tab


# V2

def resolve(tab):
	a = 0.0
	b = 0
	c = 0
	i = 0
	l = len(tab)
	while i < l:
		if str(tab[i]) == '*':
			if (tab[i + 1]) == 'X^2':
				a += tab[i - 1]
				tab[i - 1] = 0
				tab[i + 1] = 0
				tab[i] = '+'
			if (tab[i + 1]) == 'X':
				b += tab[i - 1]
				tab[i - 1] = 0
				tab[i + 1] = 0
				tab[i] = '+'
		i += 1
	for v in tab:
		if isinstance(v, float):
			c += v
	if a:
		calculate_second(a, b, c)
	else:
		calculate_simple(b, c)

def x_detail(tab):
	c = 1.0
	first = 0
	l = len(tab)
	i = 0
	while i < l:
		try:
			if first == 0:
				c *= float(tab[i])
				first = 1
			else:
				if tab[i - 1] == '*':
					c *= float(tab[i])
				elif tab[i - 1] == '/':
					c /= float(tab[i])
		except:
			pass
		i += 1
	return c

def decompose_x_detail(d, s):
	tab = s.split(' ')
	for v in tab:
		if v == 'X^0':
			d['X^0'] += x_detail(tab)
			return d
		if v == 'X^1':
			d['X^1'] += x_detail(tab)
			return d
		if v == 'X^2':
			d['X^2'] += x_detail(tab)
			return d
	d['c'] += x_detail(tab)
	return d

def decompose_x(s):
	d = {}
	d['X^0'] = 0
	d['X^1'] = 0
	d['X^2'] = 0
	d['c'] = 0
	tab = s.split('+')
	for v in tab:
		d = decompose_x_detail(d, v)
	return d


def merge_d(left_x, right_x):
	left_x['X^0'] -= right_x['X^0']
	left_x['X^1'] -= right_x['X^1']
	left_x['X^2'] -= right_x['X^2']
	left_x['c'] -= right_x['c']
	return left_x


def print_reduced_v2(d):
	s = None
	if d['X^0']:
		s = ''
		s += str(d['X^0']) + ' * X^0'
	if d['X^1']:
		if s:
			s += ' + '
		else:
			s = ''
		s += str(d['X^1']) + ' * X^1'

	if d['X^2']:
		if s:
			s += ' + '
		else:
			s = ''
		s += str(d['X^2']) + ' * X^2'

	if d['c']:
		if s:
			s += ' + '
		else:
			s = ''
		s += str(d['c'])

	s += ' = 0'
	print(s)

def v2(s):
	s = s.replace('- ', ' + -')
	s = s.replace('-X', '-1 * X')
	split = s.split('=')
	left = split[0].strip()
	right = split[1].strip()
	left_x = decompose_x(left)
	right_x = decompose_x(right)
	print(left_x)
	print(right_x)
	reduced = merge_d(left_x, right_x)
	print('\n')
	print(reduced)
	print('\n')
	print_reduced_v2(reduced)




if __name__ == '__main__':
		# resolve_simple(sys.argv[1])
		v2(sys.argv[1].strip())
		sys.exit()
		if is_infinite_solution(sys.argv[1]) == 1:
			print('Every real number are solution')
			sys.exit()
		# decompose(sys.argv[1])
		tab = sys.argv[1].strip().split('=')
		right = tab[0].strip()
		left = tab[1].strip()
		di_left = decompose_left(left)
		tab_right = decompose_right(right)
		tab_reduced = found_reduced_form(tab_right, di_left)
		print_reduced(tab_reduced)
		print_reduced_degre(tab_reduced)
		tab_reduced = replace_puissance(tab_reduced)
		tab_reduced = sort_puissance(tab_reduced)
		tab_reduced = cast_to_float(tab_reduced)
		tab_reduced = replace_less(tab_reduced)
		tab_reduced = resolve_multi(tab_reduced)
		tab_reduced = resolve_div(tab_reduced)
		resolve(tab_reduced)
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
